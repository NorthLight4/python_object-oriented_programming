class Employee:
    def __init__(self, name: str, position: str, salary: float):
        """
        Создание и подготовка к работе объекта "Работник"
        Является базовым классом
        Атрибуты:
        :param name: Имя работника.
        :param position: Должность работника.
        :param salary: Зарплата работника.
        """
        self.name = name
        self.position = position
        self.salary = salary

    def calculate_salary(self) -> float:
        """
        Метод подсчета зарплаты работника
        """
        return self.salary

    def __str__(self) -> str:
        return f"Работник {self.name}. Зарплата {self.salary}. Должность {self.position}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name}, salary = {self.salary}, position = {self.position})"



class Manager(Employee):
    def __init__(self, name: str, position: str, salary: float, projects: int):
        """
        Создание и подготовка к работе объекта "Руководитель"
        Является наследником класса "Employee"
        Атрибуты:
        :param name: Имя руководителя.
        :param position: Должность руководителя.
        :param salary: Зарплата руководителя.
        :param projects: Количество проектов руководителя.
        """
        super().__init__(name, position, salary)
        self.projects = projects

    def calculate_salary(self) -> float:
        """
        Перегруженный метод подсчета зарплаты руководителя
        Менеджеры часто имеют бонусы к заработной плате за успешное завершение задач
        """
        bonus = self.projects * 1000
        return self.salary + bonus

    def __str__(self) -> str:
        return f"{super().__str__()}(Manager). Количество проектов {self.projects}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name}, salary = {self.salary}, position = {self.position}, projects = {self.projects})"

class Intern(Employee):
    def __init__(self, name: str, position: str, salary: float, tasks_completed: int):
        """
        Создание и подготовка к работе объекта "Стажёр"
        Является наследником класса "Employee"
        Атрибуты:
        :param name: Имя стажёра.
        :param position: Должность стажёра.
        :param salary: Зарплата стажёра.
        :param tasks_completed: Количество выполненных задач стажёра.
        """
        super().__init__(name, position, salary)
        self.tasks_completed = tasks_completed

    def report_tasks(self) -> str:
        """
        Метод, который позволяет узнать количество выполненных задач стажёра
        """
        return f"Интерн {self.name}. Выполнено задач: {self.tasks_completed}"

    def __str__(self) -> str:
        return f"{super().__str__()}(Intern)"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name = {self.name}, salary = {self.salary}, position = {self.position}, tasks_completed = {self.tasks_completed})"