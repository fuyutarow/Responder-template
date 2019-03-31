import graphene
from .dodoit import QueryDodoit, CreateDodoit


class Query(
        QueryDodoit, ):
    pass


class Mutation(graphene.ObjectType):
    create_dodoit = CreateDodoit.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
