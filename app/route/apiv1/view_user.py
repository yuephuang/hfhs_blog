from flask_restx import Namespace, Resource, fields
from app.operation.user_operation import UserOperation

api = Namespace('user', description='user相关配置', path="/user")


class LoginExpect:
    @staticmethod
    def get():
        parser = api.parser()
        parser.add_argument("id", location="args", required=True)
        return parser


class RegisterExpect:
    @staticmethod
    def get():
        parser = api.parser()
        return parser

    @staticmethod
    def post():
        parser = api.parser()
        parser.add_argument("user_name", location="json", required=True)
        parser.add_argument("password", location="json", required=True)
        parser.add_argument("gender", location="json")
        parser.add_argument("email", location="json", required=True)
        parser.add_argument("phone", location="json", required=True)
        parser.add_argument("age", location="json")
        parser.add_argument("follow", location="json")
        parser.add_argument("fans", location="json")
        return parser


class LoginModel:
    @staticmethod
    def get():
        model = api.model(
            "User_Login_Get",
            {
                "id": fields.Integer(description='用户id'),
                "user_name": fields.String(description='用户名字'),
                "gender": fields.String(description='用户性别'),
                "email": fields.String(description='用户邮箱'),
                "phone": fields.String(description='用户电话'),
                "age": fields.String(description='用户年龄'),
                "follow": fields.String(description='用户关注的人'),
                "fans": fields.Integer(description='用户粉丝', default=0),
            }
        )

        return model


class RegisterModel:
    @staticmethod
    def get():
        model = api.model(
            "User_register_Get",
            {

            }
        )

        return model

    @staticmethod
    def post():
        model = api.model(
            "User_register_Post",
            {
                "job_id": fields.String(),
                "status": fields.String(),
                "message": fields.String()
            }
        )

        return model


@api.route("/login")
class UserLogin(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = UserOperation()

    get_parser = LoginExpect.get()

    @api.expect(get_parser)
    @api.marshal_with(LoginModel.get())
    def get(self):
        parser = self.get_parser.parse_args()
        _id = int(parser.get("id", -1))
        result = self.user.get_user_info(_id=_id)
        return result


@api.route("/register")
class UserRegister(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = UserOperation()

    get_parser = RegisterExpect.get()
    post_parser = RegisterExpect.post()

    # @api.expect(get_parser)
    # @api.marshal_with(RegisterModel.get())
    def get(self):
        pass

    @api.expect(post_parser)
    @api.marshal_with(RegisterModel.post())
    def post(self):
        parser = self.post_parser.parse_args()
        result = self.user.register_user(parser)
        return {
            "job_id": "id",
            "status": "success" if result else "fail",
            "message": ""
        }