# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

# TODO: Authorizations
# authorizations = {
#     'apikey': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'X-API-KEY'
#     }
# }

api = Api(blueprint,
          title='Credit Swag RestPlus Backend',
          version='1.0',
          # authorizations=authorizations,
          description='fintech for students by students'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)