from dao.model.movie import Movie
from config import Config


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, movie_id):
        return self.session.query(Movie).get(movie_id)

    def get_all(self, filter):
        status = filter.get("status")
        page = filter.get("page")

        if status == "new" and page is not None:
            return self.session.query(Movie).order_by(Movie.year.desc()).\
                paginate(int(page), Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
        elif status == "new":
            return self.session.query(Movie).order_by(Movie.year.desc()).all()
        elif page is not None:
            return self.session.query(Movie).\
                paginate(int(page), Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Movie).all()

    def get_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, movie_data):
        new_movie = Movie(**movie_data)
        self.session.add(new_movie)
        self.session.commit()
        return new_movie

    def delete(self, movie_id):
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_data):
        movie = self.get_one(movie_data.get("id"))
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")
        self.session.add(movie)
        self.session.commit()
