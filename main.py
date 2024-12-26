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


# Main Function Wrapper
def main():
    connection = get_connection("subscribers.db")

    # Create the table
    create_table(connection)


if __name__ == "__main__":
    main()
