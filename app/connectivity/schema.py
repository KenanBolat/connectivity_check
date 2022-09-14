import graphene
from graphene_django import DjangoObjectType
from .models import Connectivity


class ConnectivityType(DjangoObjectType):
    class Meta:
        model = Connectivity
        fields = ("id", "IP", "description",
                  "is_accessible", "is_enabled",
                  "update_date")


class Query(graphene.ObjectType):
    all_connectees = graphene.List(ConnectivityType)
    def resolve_all_connectees(root, info):
        # return Connectivity.objects.all()
        return Connectivity.objects.filter(id='1')



schema = graphene.Schema(query=Query)
