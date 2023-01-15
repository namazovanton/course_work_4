from config import Config
from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, genre_id):
        return self.session.query(Genre).get(genre_id)

    def get_all(self, filter):
        page = filter.get("page")
        if page is not None:
            return self.session.query(Genre).\
                paginate(int(page), Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Genre).all()

    def create(self, genre_data):
        new_genre = Genre(**genre_data)
        self.session.add(new_genre)
        self.session.commit()
        return new_genre

    def delete(self, genre_id):
        genre = self.get_one(genre_id)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_data):
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")
        self.session.add(genre)
        self.session.commit()
