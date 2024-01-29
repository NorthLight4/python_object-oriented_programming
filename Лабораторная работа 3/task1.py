class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        if not isinstance(pages, int):
            raise TypeError("Атрибут pages должен быть int")
        if pages < 0:
            raise ValueError("Атрибут pages не может быть отрицательным числом")
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()}. Кол-во страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name,author)
        if not isinstance(duration, (float,int)):
            raise TypeError("Атрибут duration должен быть числом")
        if duration < 0:
            raise ValueError("Атрибут duration не может быть отрицательным числом")
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"