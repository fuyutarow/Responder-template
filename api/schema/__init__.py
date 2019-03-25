import graphene
from .vine import QueryVine, CreateVine
from .tomato import QueryTomato, CreateTomato


class Query(
        QueryVine,
        QueryTomato,
):
    pass


class Mutation(graphene.ObjectType):
    create_vine = CreateVine.Field()
    create_tomato = CreateTomato.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
