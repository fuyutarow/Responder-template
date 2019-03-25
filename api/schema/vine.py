import graphene
from graphene_django.types import DjangoObjectType

from api.models import Vine


class VineType(DjangoObjectType):
    class Meta:
        model = Vine


class QueryVine(graphene.ObjectType):
    all_vines = graphene.List(VineType)
    vine = graphene.Field(VineType, id=graphene.Int(), name=graphene.String())

    def resolve_all_vines(self, info, **kwargs):
        return Vine.objects.all()

    def resolve_vine(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Vine.objects.get(pk=id)

        if name is not None:
            return Vine.objects.get(name=name)

        return None


class CreateVine(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    # vine = graphene.Field(lambda: VineType)
    vine = graphene.Field(VineType)

    @staticmethod
    def mutate(root, info, name):
        vine = Vine.objects.create(name=name)
        return CreateVine(vine=vine)
