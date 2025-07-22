from .person import Person


class Admin(Person):
    """
    Represents an admin entity inheriting from Person, with a fixed role of 'admin'.

    Overrides:
        get_role(): Returns the string 'admin' to indicate the admin's role.
    """
    def get_role(self) -> str:
        return "admin"
