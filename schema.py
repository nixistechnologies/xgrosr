import graphene
import app.schema

#class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
#    pass

# class Mutation(app.schema.Mutation,graphene.ObjectType):
#     social_auth = graphql_social_auth.SocialAuthJWT.Field()
    # pass

class Query(app.schema.Query,graphene.ObjectType):
    pass
# class Subscription(app.schema.Subscription,graphene.ObjectType):
#     pass 

schema = graphene.Schema(query=Query,
# mutation=Mutation
)