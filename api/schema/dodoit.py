import graphene
from graphene_django.types import DjangoObjectType

from api.models import Dodoit


class TypeDodoit(DjangoObjectType):
    class Meta:
        model = Dodoit


class QueryDodoit(graphene.ObjectType):
    dodoits = graphene.List(TypeDodoit)
    dodoit = graphene.Field(
        TypeDodoit, id=graphene.Int(), content=graphene.String())

    def resolve_dodoits(self, info, **kwargs):
        return Dodoit.objects.all()

    def resolve_dodoit(self, info, **kwargs):
        id = kwargs.get('id')
        content = kwargs.get('content')

        if id is not None:
            return Dodoit.objects.get(pk=id)

        if content is not None:
            return Dodoit.objects.get(content=content)

        return None


class CreateDodoit(graphene.Mutation):
    class Arguments:
        content = graphene.String()

    dodoit = graphene.Field(TypeDodoit)

    @staticmethod
    def mutate(root, info, content):
        dodoit = Dodoit.objects.create(content=content)
        return CreateDodoit(dodoit=dodoit)


class CreateDodoits(graphene.Mutation):
    class Arguments:
        content = graphene.String()

    dodoits = graphene.List(TypeDodoit)

    @staticmethod
    def mutate(root, info, content):
        dodoits = Dodoit.objects.bulk_create(content=content)
        return CreateDodoits(dodoits=dodoits)
