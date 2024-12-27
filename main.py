# All the imports
import sqlite3
from icecream import ic as print


# Setup / Initialization of the database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise


# Create a table in the database
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT UNIQUE
    );
    """
    try:
        with connection:
            connection.execute(query)
        print("Table created successfully")
    except Exception as e:
        print(e)


# Add user to database
def insert_user(connection, name: str, age: int, email: str):
    query = """
    INSERT INTO users (name, age, email) VALUES (?, ?, ?);
    """
    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"User: {name} added successfully")
    except Exception as e:
        print(e)


# Query all users in database
def fetch_users(connection, condition: str = None) -> list[tuple]:
    query = """
    SELECT * FROM users;
    """
    if condition:
        query += f" WHERE {condition}"

    try:
        with connection:
            rows = connection.execute(query).fetchall()
            return rows
    except Exception as e:
        print(e)


# Delete user from database
def delete_user(connection, user_id: int):
    query = """
    DELETE FROM users WHERE id = ?;
    """
    try:
        with connection:
            connection.execute(query, (user_id,))
        print(f"User: {user_id} was deleted successfully")
    except Exception as e:
        print(e)


# Update user in database
def update_user(connection, user_id: int, email: str):
    query = """
    UPDATE users SET email = ? WHERE id = ?;
    """
    try:
        with connection:
            connection.execute(query, (email, user_id))
        print(f"User: {user_id} has new email {email} successfully")
    except Exception as e:
        print(e)


# Ability to add many users at once
def add_many_users(connection, users: list[tuple[str, int, str]]):
    query = """
    INSERT INTO users (name, age, email) VALUES (?, ?, ?);
    """
    try:
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} users added successfully")
    except Exception as e:
        print(e)


# Main Function Wrapper
def main():
    connection = get_connection("subscribers.db")

    try:
        # Create the table
        create_table(connection)

        x = int(input("1 - activate, 2 - freeze: "))
        while x != 2:
            start = input(
                "Enter option (Add, Delete, Update, Search, Add Many): "
            ).lower()

            if start == "add":
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                email = input("Enter email: ")
                insert_user(connection, name, age, email)
            elif start == "search":
                print("All users:")
                for user in fetch_users(connection):
                    print(user)
            elif start == "delete":
                user_id = int(input("Enter user id: "))
                delete_user(connection, user_id)
            elif start == "update":
                user_id = int(input("Enter user id: "))
                new_email = input("Enter new email: ")
                update_user(connection, user_id, new_email)
            elif start == "add many":
                users = [
                    ("John", 25, "john@example.com"),
                    ("Jane", 30, "jane@example.com"),
                    ("Bob", 40, "bob@example.com"),
                ]
                add_many_users(connection, users)

            x = int(input("1 - activate, 2 - freeze: "))

    finally:
        connection.close()


if __name__ == "__main__":
    main()
