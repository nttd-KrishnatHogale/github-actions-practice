import os
import psycopg2


def connect_database():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        database=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "testuser"),
        password=os.getenv("DB_PASSWORD", "testpassword")
    )


def check_database():
    connection = connect_database()

    cursor = connection.cursor()
    cursor.execute("SELECT 1;")

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result[0]


if __name__ == "__main__":
    result = check_database()
    print(f"Database test result: {result}")