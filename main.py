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


# Main Function Wrapper
def main():
    connection = get_connection("subscribers.db")


if __name__ == "__main__":
    main()
