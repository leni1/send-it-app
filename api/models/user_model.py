import attr

from datetime import datetime

@attr.s(auto_attribs=True, slots=True)
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

        user_id = attr.ib(validator=attr.validators.instance_of(int))
        firstname = attr.ib(validator=attr.validators.instance_of(str))
        lastname = attr.ib(validator=attr.validators.instance_of(str))
        othername = attr.ib(validator=attr.validators.instance_of(str))
        email = attr.ib(validator=attr.validators.instance_of(str))
        username = attr.ib(validator=attr.validators.instance_of(str))
        reg_date = attr.ib(validator=attr.validators.instance_of(datetime))
        is_admin = attr.ib(validator=attr.validators.instance_of(bool))

