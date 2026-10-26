# from app import get_message


# def test_message():
#     assert get_message() == "GitHub Actions Cache and Artifact Demo"
from app import greet


def test_greet():
    assert greet("GitHub") == "Hello, GitHub!"