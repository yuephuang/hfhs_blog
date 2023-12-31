from flask_restx import Api
from app.route.apiv1.view_test import api as test_api
from app.route.apiv1.view_user import api as user_api

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(test_api, path='/test')
api.add_namespace(user_api)