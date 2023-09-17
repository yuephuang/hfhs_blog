from flask_restx import Namespace, Resource, fields

api = Namespace('test', description='blog')

model = api.model(
    "test",
    {"id": fields.Integer()}
)


@api.route('/<id>')
@api.param('id', 'The cat identifier')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(model)
    def get(self, id):
        """Fetch a cat given its identifier"""
        return id
