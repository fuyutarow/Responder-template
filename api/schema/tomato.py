import graphene
from graphene_django.types import DjangoObjectType

from api.models import Tomato


class TomatoType(DjangoObjectType):
    class Meta:
        model = Tomato


class QueryTomato(graphene.ObjectType):
    all_tomatos = graphene.List(TomatoType)
    tomato = graphene.Field(
        TomatoType, id=graphene.Int(), name=graphene.String())

    def resolve_all_tomatos(self, info, **kwargs):
        return Tomato.objects.all()

    def resolve_tomato(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Tomato.objects.get(pk=id)

        if name is not None:
            return Tomato.objects.get(name=name)

        return None


class CreateTomato(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    tomato = graphene.Field(TomatoType)

    @staticmethod
    def mutate(root, info, name):
        tomato = Tomato.objects.create(name=name)
        return CreateTomato(tomato=tomato)
