from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, director_id):
        return self.dao.get_one(director_id)

    def get_all(self, filter):
        directors = self.dao.get_all(filter)
        return directors

    def create(self, director_data):
        return self.dao.create(director_data)

    def update(self, director_data):
        self.dao.update(director_data)
        return self.dao

    def delete(self, director_id):
        self.dao.delete(director_id)