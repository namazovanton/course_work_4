from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, genre_id):
        return self.dao.get_one(genre_id)

    def get_all(self, filter):
        genres = self.dao.get_all(filter)
        return genres

    def create(self, genre_data):
        return self.dao.create(genre_data)

    def update(self, genre_data):
        self.dao.update(genre_data)
        return self.dao

    def delete(self, genre_id):
        self.dao.delete(genre_id)
