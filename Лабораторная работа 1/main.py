import doctest


class Car:
    def __init__(self, brand: str, model: str, production_year: int):
        """
        Создание и подготовка к работе объекта "Стакан"

        Атрибуты:
        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param production_year: Год производства автомобиля.

        Примеры:
        >>> car = Car("Tesla", "Model S", 2010)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model

        if not isinstance(production_year, int):
            raise TypeError("Год производства должен быть int")
        if production_year < 0:
            raise ValueError("Год не может быть отрицательным числом")
        self.production_year = production_year

    def start_engine(self) -> None:
        """
        Метод для запуска двигателя автомобиля.

        Примеры:
        >>> car = Car("Tesla", "Model S", 2010)
        >>> car.start_engine()
        """
        ...

    def drive(self, destination: str) -> None:
        """
        Метод для езды к указанному месту.
        :param destination: Пункт назначения

        Примеры:
        >>> car = Car("Tesla", "Model S", 2010)
        >>> car.drive("Уфа")
        """
        if not isinstance(destination, str):
            raise TypeError("Параметр должен быть типа str")
        ...

    def stop(self) -> None:
        """
        Метод для остановки автомобиля.

        Примеры:
        >>> car = Car("Tesla", "Model S", 2010)
        >>> car.stop()
        """
        ...


class Smartphone:
    def __init__(self, brand: str, model: str, storage_capacity: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        Атрибуты:
        :param brand: Марка смартфона.
        :param model: Модель смартфона.
        :param storage_capacity: Объем встроенной памяти смартфона в Гб.

        Примеры:
        >>> smartphone = Smartphone("OnePlus", "12", 256)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть типа str")
        self.model = model

        if not isinstance(storage_capacity, int):
            raise TypeError("Объем памяти должен быть int")
        if storage_capacity < 0:
            raise ValueError("Объем памяти не может быть отрицательным числом")
        self.storage_capacity = storage_capacity

    def make_call(self, phone_number: str) -> None:
        """
       Метод для осуществления звонка.
       :param phone_number: Номер телефона

        Примеры:
        >>> smartphone = Smartphone("OnePlus", "12", 256)
        >>> smartphone.make_call("888888888")
        """
        if not isinstance(phone_number, str):
            raise TypeError("Параметр должен быть типа str")
        ...

    def send_text(self, recipient: str, message: str) -> None:
        """
        Метод для отправки текстового сообщения.
        :param recipient: Получатель
        :param message: Текст сообщения

        Примеры:
        >>> smartphone = Smartphone("OnePlus", "12", 256)
        >>> smartphone.send_text("Паша Техник", "Йоу")
        """
        if not isinstance(recipient, str):
            raise TypeError("Параметр должен быть типа str")
        if not isinstance(message, str):
            raise TypeError("Параметр должен быть типа str")
        ...

    def take_photo(self) -> None:
        """
        Метод для съемки фотографии.

        Примеры:
        >>> smartphone = Smartphone("OnePlus", "12", 256)
        >>> smartphone.take_photo()
        """
        ...


class BankAccount:
    def __init__(self, account_number: str, balance: float):
        """
        Создание и подготовка к работе объекта "Банковский аккаунт"

        Атрибуты:
        :param account_number: Номер банковского счета
        :param balance: Баланс на счёте

        Примеры:
        >>> bankAccount = BankAccount("23123123", 2510.5)  # инициализация экземпляра класса
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер должен быть типа str")
        self.account_number = account_number

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть float")
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
       Метод для внесения денежных средств на счет.
       :param amount: количество

        Примеры:
        >>> bankAccount = BankAccount("23123123", 2510.5)
        >>> bankAccount.deposit(200.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Параметр должен быть типа float")
        if amount < 0:
            raise ValueError("Количество не может быть отрицательным числом")
        ...

    def withdraw(self, amount: float) -> None:
        """
        Метод для снятия денежных средств со счета.
        :param amount: количество

        Примеры:
        >>> bankAccount = BankAccount("23123123", 2510.5)
        >>> bankAccount.withdraw(2000.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Параметр должен быть типа float")
        if amount < 0:
            raise ValueError("Количество не может быть отрицательным числом")
        ...

    def check_balance(self) -> float:
        """
        Метод для проверки баланса счета
        :return: Количество средств

        Примеры:
        >>> bankAccount = BankAccount("23123123", 2510.5)
        >>> bankAccount.check_balance()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации