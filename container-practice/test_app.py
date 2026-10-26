from app import check_database


def test_database_connection():
    assert check_database() == 1