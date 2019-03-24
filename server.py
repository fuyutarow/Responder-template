import responder
import graphene

api = responder.API()


@api.route("/")
async def upload_file(req, resp):
    @api.background.task
    def process_data(data):
        f = open('./{}'.format(data['file']['filename']), 'w')
        f.write(data['file']['content'].decode('utf-8'))
        f.close()

    data = await req.media(format='files')
    process_data(data)

    resp.media = {'success': 'ok'}


@api.route('/hello/{who}')
def hello_to(request, response, *, who):
    response.media = {'who': who}


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"


schema = graphene.Schema(query=Query)
view = responder.ext.GraphQLView(api=api, schema=schema)
api.add_route("/graphql", view)

if __name__ == "__main__":
    api.run(debug=True)
    # api.run()
