from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def get_all(self, filters):
        movies = self.dao.get_all(filters)
        return movies

    def create(self, movie_data):
        return self.dao.create(movie_data)

    def update(self, movie_data):
        self.dao.update(movie_data)
        return self.dao

    def delete(self, movie_id):
        self.dao.delete(movie_id)
