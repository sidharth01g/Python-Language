import sqlite3


def main():

    try:
        # Create DB connection'
        connection1 = sqlite3.connect("test.db")

        # Create a cursor object
        cursor1 = connection1.cursor()

        # Execute a query

        #cursor1.execute("CREATE TABLE Items(Id INT, Name TEXT, Price INT)")
        cursor1.execute("INSERT INTO Items VALUES(1, 'Glue', 30)")
        cursor1.execute("INSERT INTO Items VALUES(2, 'Pen', 10)")
        cursor1.execute("INSERT INTO Items VALUES(3, 'Notepad', 100)")
        connection1.commit()


        cursor1.execute("SELECT * FROM Items")
        # Fetch query result
        # data = cursor1.fetchone()
        data = cursor1.fetchall()
        for row in data:
            print row
    except sqlite3.Error, error:
        print("Exception: " + str(error))
        if connection1:
            connection1.rollback()
    finally:
        if connection1:
            connection1.close()

    # Close connection
    connection1.close()


if __name__ == "__main__":
    main()
