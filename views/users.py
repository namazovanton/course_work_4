from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from decorators import auth_required
from implemented import user_service

user_ns = Namespace('user')


@user_ns.route("/")
class UsersView(Resource):
    @auth_required
    def get(self):
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)
        return response, 200

    @auth_required
    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route("/<int:uid>")
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)
        response = UserSchema().dump(user)
        return response, 200

    @auth_required
    def patch(self, uid):
        req_json = request.json
        if "id" not in req_json:
            req_json["id"] = uid
        user_service.update(req_json)
        return f"User with id = {uid} updated", 204

    @auth_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204


@user_ns.route("/password")
class UserPasswordView(Resource):
    @auth_required
    def put(self):
        user_data = request.json
        email = user_data.get("email")
        old_password = user_data.get("old_password")
        new_password = user_data.get("new_password")

        user = user_service.get_user_by_email(email)

        if user_service.compare_passwords(user.password, old_password):
            user.password = user_service.generate_password(new_password)
            result = UserSchema().dump(user)
            user_service.update(result)

        return "", 201

