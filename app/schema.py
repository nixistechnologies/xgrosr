import graphene
from django.contrib.auth.models import User,Group
from app.models import *
from graphene_django.fields import DjangoConnectionField
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id
from graphene import relay

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields =  ()
        interfaces = (relay.Node,)


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields =  ()
        interfaces = (relay.Node,)


class Query(graphene.AbstractType):
    products = DjangoFilterConnectionField(ProductNode)
    categorys = DjangoFilterConnectionField(CategoryNode)