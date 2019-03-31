import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
from django.apps import apps
from django.conf import settings
apps.populate(settings.INSTALLED_APPS)

import responder
import graphene
api = responder.API(
    cors=True,
    allowed_hosts=["*"],
)

from api.schema import schema
view = responder.ext.GraphQLView(api=api, schema=schema)
api.add_route("/graphql", view)


@api.route('/')
def redirect_home(request, response):
    api.redirect(response, '/graphql')


if __name__ == "__main__":
    # api.run(debug=True)
    api.run()
