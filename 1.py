import mysql.connector
from mysql.connector import Error
def add_member(id, name, age):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            database='test',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to add a new member
            sql_insert_query = """INSERT INTO Members (id, name, age) 
                                  VALUES (%s, %s, %s)"""
            # Tuple of data to insert
            insert_tuple = (id, name, age)

            # Execute the query
            cursor.execute(sql_insert_query, insert_tuple)

            # Commit the transaction
            connection.commit()

            print("New member added successfully")

    except Error as e:
        print(f"Error: {e}")
        # Rollback the transaction in case of error
        if connection.is_connected():
            connection.rollback()

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#2

def add_workout_session(member_id, session_date, session_time, activity):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            database='test',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL query to add a new workout session
            sql_insert_query = """INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) 
                                  VALUES (%s, %s, %s, %s)"""
            # Tuple of data to insert
            insert_tuple = (member_id, session_date, session_time, activity)

            # Execute the query
            cursor.execute(sql_insert_query, insert_tuple)

            # Commit the transaction
            connection.commit()

            print("New workout session added successfully")

    except Error as e:
        print(f"Error: {e}")
        # Rollback the transaction in case of error
        if connection.is_connected():
            connection.rollback()

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#3
def update_member_age(member_id, new_age):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            database='test',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the member exists
            check_member_query = "SELECT COUNT(*) FROM Members WHERE id = %s"
            cursor.execute(check_member_query, (member_id,))
            member_exists = cursor.fetchone()[0]

            if member_exists:
                # SQL query to update age
                update_age_query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(update_age_query, (new_age, member_id))

                # Commit the transaction
                connection.commit()

                print(f"Member ID {member_id}'s age updated to {new_age}")
            else:
                print(f"Member ID {member_id} not found")

    except Error as e:
        print(f"Error: {e}")
        # Rollback the transaction in case of error
        if connection.is_connected():
            connection.rollback()

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


#4

def delete_workout_session(session_id):
    try:
        # Establish the database connection
        connection = mysql.connector.connect(
            database='test',
            user='root',
            password='your_password'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the session ID exists
            check_session_query = "SELECT COUNT(*) FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_session_query, (session_id,))
            session_exists = cursor.fetchone()[0]

            if session_exists:
                # SQL query to delete the session
                delete_session_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_session_query, (session_id,))

                # Commit the transaction
                connection.commit()

                print(f"Workout session ID {session_id} deleted successfully")
            else:
                print(f"Workout session ID {session_id} not found")

    except Error as e:
        print(f"Error: {e}")
        # Rollback the transaction in case of error
        if connection.is_connected():
            connection.rollback()

    finally:
        # Close the cursor and connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")