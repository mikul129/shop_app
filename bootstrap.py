import mysql.connector

connection = None
cursor = None

def init():
    global connection
    connection = mysql.connector.connect(host="localhost", user="root", password="admin", database="mydb")
    global cursor
    cursor = connection.cursor()

def close():
    connection.close()
    cursor.close()

def commit():
    connection.commit()

def get_connection():
    return(connection)

def get_cursor():
    return(cursor)


