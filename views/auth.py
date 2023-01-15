from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route("/register")
class AuthViewRegister(Resource):
    def post(self):
        data = request.json

        email = data.get("email")
        password = data.get("password")
        if None in [email, password]:
            return "", 400

        user_service.create(data)
        return "", 201


@auth_ns.route("/login")
class AuthViewLogin(Resource):
    def post(self):
        data = request.json
        print(data)
        email = data.get("email")
        password = data.get("password")
        if None in [email, password]:
            return "", 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):
        data = request.json
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        is_validated = auth_service.validate_tokens(access_token, refresh_token)

        if not is_validated:
            return "Invalid token", 400

        tokens = auth_service.approve_refresh_token(refresh_token)
        return tokens, 201
