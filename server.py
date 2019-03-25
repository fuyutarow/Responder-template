import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
from django.apps import apps
from django.conf import settings
apps.populate(settings.INSTALLED_APPS)

import responder
import graphene
api = responder.API()

from api.schema import schema
view = responder.ext.GraphQLView(api=api, schema=schema)
api.add_route("/graphql", view)


@api.route("/")
async def upload_file(req, resp):
    @api.background.task
    def process_data(data):
        with open('./{}'.format(data['file']['filename']), 'w') as f:
            f.write(data['file']['content'].decode('utf-8'))

    data = await req.media(format='files')
    process_data(data)

    resp.media = {'success': 'ok'}


@api.route('/hello/{who}')
def hello_to(request, response, *, who):
    response.media = {'who': who}


import time


@api.route("/incoming")
async def receive_incoming(req, resp):
    @api.background.task
    def process_data(data):
        """Just sleeps for three seconds, as a demo."""
        time.sleep(3)

    # Parse the incoming data as form-encoded.
    # Note: 'json' and 'yaml' formats are also automatically supported.
    data = await req.media()

    # Process the data (in the background).
    process_data(data)

    # Immediately respond that upload was successful.
    resp.media = {'success': True}


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return f"Hello {name}"


schema = graphene.Schema(query=Query)
view = responder.ext.GraphQLView(api=api, schema=schema)
api.add_route("/g/hello", view)

if __name__ == "__main__":
    api.run(debug=True)
    # api.run()
