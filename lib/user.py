# lib/testing/user_test.py
from user import User

def test_user_init():
    user = User("John", "Doe")
    assert user.first_name == "John"
    assert user.last_name == "Doe"

def test_user_attributes():
    user = User("Jane", "Smith")
    assert hasattr(user, "first_name")
    assert hasattr(user, "last_name")

    assert user.first_name == "Jane"
    assert user.last_name == "Smith"
