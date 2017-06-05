import sqlite3


def main():

    # Create DB connection'
    connection1 = sqlite3.connect("test.db")

    # Create a cursor object
    cursor1 = connection1.cursor()

    # Execute a query
    cursor1.execute("SELECT SQLITE_VERSION()")
    # Fetch query result
    data = cursor1.fetchone()
    print data

    # Close connection
    connection1.close()


if __name__ == "__main__":
    main()
