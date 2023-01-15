from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        entity = User(**user_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, user_data):
        user = self.get_one(user_data.get("id"))
        for keys, values in user_data.items():
            setattr(user, keys, values)
        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()
