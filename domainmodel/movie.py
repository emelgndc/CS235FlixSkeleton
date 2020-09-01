from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title: str, release_year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()

        if release_year < 1900 or type(release_year) is not int:
            self.__release_year = None
        else:
            self.__release_year = release_year

        self.__director = None
        self.__description = ""
        self.__actors = []
        self.__genres = []
        self.__runtime_minutes = 0

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        if type(title) is str:
            self.__title = title.strip()

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, release_year: int):
        if type(release_year) is int:
            if release_year >= 1900:
                self.__release_year = release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        if type(description) is str:
            self.__description = description.strip()

    @property
    def director(self) -> str:
        return self.__director

    @director.setter
    def director(self, director: Director):
        if type(director) is Director:
            self.__director = director

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors: list):
        allactors = True
        if type(actors) is list:
            for i in actors:
                if type(i) is not Actor:
                    allactors = False
            if allactors:
                self.__actors = actors

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genres: list):
        allgenres = True
        if type(genres) is list:
            for i in genres:
                if type(i) is not Genre:
                    allgenres = False
            if allgenres:
                self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, num: int):
        if type(num) is int:
            if num > 0:
                self.__runtime_minutes = num
            else:
                raise ValueError
        else:
            raise ValueError

    def add_actor(self, actor: Actor):
        if type(actor) is Actor:
            self.__actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.__actors:
            self.__actors.remove(actor)

    def add_genre(self, genre: Genre):
        if type(genre) is Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.__genres:
            self.__genres.remove(genre)
        
    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return self.__title == other.__title and self.__release_year == other.__release_year

    def __lt__(self, other):
        if self.__title == other.__title:
            return self.__release_year < other.__release_year
        else:
            return self.title < other.title

    def __hash__(self):
        return hash((self.__title, self.__release_year))
