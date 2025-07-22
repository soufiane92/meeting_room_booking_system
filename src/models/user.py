from .person import Person


class User(Person):
    """
    Represents a user entity inheriting from Person, with a fixed role of 'user'.

    Overrides:
        get_role(): Returns the string 'user' to indicate the user's role.
    """
    def get_role(self) -> str:
        return "user"
