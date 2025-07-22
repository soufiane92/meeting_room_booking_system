from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, email:str):
        self._name = name
        self._email = email

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @abstractmethod
    def get_role(self) -> str:
        pass
