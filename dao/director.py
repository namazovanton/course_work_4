from config import Config
from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, director_id):
        return self.session.query(Director).get(director_id)

    def get_all(self, filter):
        page = filter.get("page")
        if page is not None:
            return self.session.query(Director).\
                paginate(int(page), Config.ITEMS_PER_PAGE, max_per_page=Config.MAX_PAGE).items
        return self.session.query(Director).all()

    def create(self, director_data):
        new_director = Director(**director_data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def delete(self, director_id):
        director = self.get_one(director_id)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_data):
        director = self.get_one(director_data.get("id"))
        director.name = director_data.get("name")
        self.session.add(director)
        self.session.commit()
