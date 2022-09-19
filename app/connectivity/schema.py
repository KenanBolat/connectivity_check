import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from .models import Connectivity


class ConnectivityType(DjangoObjectType):
    class Meta:
        model = Connectivity
        fields = ("id",
                  "ip",
                  "description",
                  "is_accessible",
                  "is_enabled",
                  "update_date",)


class Query(graphene.ObjectType):
    all_connections = graphene.List(ConnectivityType)
    connnection_by_ip = graphene.Field(ConnectivityType, ip=graphene.String())

    def resolve_all_connections(root, info):
        return Connectivity.objects.all()

    def resolve_connnection_by_ip(root, info, ip):
        return Connectivity.objects.get(IP=ip)[:0]


schema = graphene.Schema(query=Query)
