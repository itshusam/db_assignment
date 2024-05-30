import mysql.connector
from mysql.connector import Error

def get_members_in_age_range(start_age, end_age):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            database='test',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query using BETWEEN to retrieve members in the specified age range
            query = """
                SELECT id, name, age
                FROM Members
                WHERE age BETWEEN %s AND %s
            """
            cursor.execute(query, (start_age, end_age))

            # Fetch all the results
            members = cursor.fetchall()

            # Print the results
            for member in members:
                print(f"ID: {member[0]}, Name: {member[1]}, Age: {member[2]}")

    except Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")