import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_user_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = self.generate_password(user_data.get("password"))
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    # def update_info(self, user_data):
    #     uid = user_data.get("id")
    #     user = self.dao.get_one(uid)
    #     if "name" in user_data:
    #         user.name = user_data.get("description")
    #     if "surname" in user_data:
    #         user.surname = user_data.get("trailer")
    #     if "favorite_genre" in user_data:
    #         user.favorite_genre = user_data.get("year")
    #     self.dao.update(user)

    def delete(self, uid):
        self.dao.delete(uid)

    def generate_password(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, password_hash, other_password) -> bool:
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hmac.compare_digest(decoded_digest, hash_digest)