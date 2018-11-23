from datetime import date


class User:
    """User class

    User class that has the attributes we wish to store
    about users.

    Attributes:
        user_id: The user's unique id.
        firstname: The user's first name.
        lastname: The user's last name.
        othername: Will typically store the user's middle name. Otherwise
        stores any other names that the user submits.
        email: The user's e-mail address.
        username: The user's username for the application
        reg_date: The user's date of registration.
        is_admin: Tells us whether a user is an admin or not."""

    def __init__(self, user_id, firstname, lastname, othername, email, username, reg_date, is_admin):
        """Initializes the class with its attributes"""

        self.user_id = int(user_id)
        self.firstname = str(firstname)
        self.lastname = str(lastname)
        self.othername = str(othername)
        self.email = str(email)
        self.username = str(username)
        self.reg_date = date(reg_date)
        self.is_admin = bool(is_admin)
