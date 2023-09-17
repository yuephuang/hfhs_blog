from flask_restx import Namespace, Resource, fields


api = Namespace('blog', description='blog')

model = api.model(
    {}
)