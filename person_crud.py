from itertools import count
from multiprocessing.dummy import connection

import pymysql

def connect_db():
    try:
        connection =pymysql.connect(user = 'root', password = 'A9fN@ngh5', port = 3306 ,database = 'jeevan', charset = 'utf8', host = 'localhost')
        print("DB connected")
        return connection
    except:
        print("DB connection failed")
        
def disconnect_db(connection):        
    try:    
        connection.close()
        print("DB disconnected")
    except:
        print("DB disconnection failed")

def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS people (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(64) NOT NULL,gender BOOL NOT NULL, age INT DEFAULT 0,location VARCHAR(32)); '''
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        print("Table created successfully")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print("Table creation failed")
        print(e)

def read_person():
    name=input("Enter person name: ")
    age=int(input("Enter person age: "))
    gender=input("Enter person gender(m/f): ")
    location=input("Enter person location: ")
    if gender.lower() == "f":
        gender = True
    else:
        gender = False
    return (name,gender,age,location)

def create_person():
    query = """INSERT INTO people(name, gender, age, location) VALUES (%s, %s, %s, %s); """

    try:
        person = read_person()
        connection = connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query, person)
        connection.commit()
        print(f"count: {count}")
        if count == 1:
            print("Person created successfully")
        else:
            print("Person creation failed")

        cursor.close()
        disconnect_db(connection)

    except Exception as e:
        print("Person creation failed")
        print(e)

def search_person():
    id = int(input("Enter person id to be searched: "))
    query = f'select * from people where id= {id};'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        print(f"count: {count}")
        if count == 1:
            row = cursor.fetchall()
            print(row)
            print(type(row))
        else:
            print("No people found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except :
        print("Failed to list people")

def update_person():
   id = int(input("Enter person id to be updated: "))
   new_location = input("Enter new location: ")
   query = "UPDATE people SET location = %s WHERE id = %s;"
   try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query, (new_location, id))
        connection.commit()
        cursor.close()
        disconnect_db(connection)
        print()
        if count == 1:
            row = cursor.fetchone()
            print(row)
            print(type(row))
        else:
            print("No people found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except :
        print("Failed to list people")

def delete_person():
    def delete_row(self, id):
        id = int(input('Enter Id of the person to delete: '))
        query = f'delete from people where id = {id}'
        connection = self.connect_db()
        cursor = connection.cursor()
        count = cursor.execute(query)
        if count == 0:
            print(f'Person with id = {id} not found')
        else:
            print(f'Person with id = {id} deleted')
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
def list_people():
    query = 'select * from people;'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        print(f"count: {count}")
        if count == 1:
            row = cursor.fetchone()
            print(row)
            print(type(row))
        else:
            print("No people found")
        connection.commit()
        cursor.close()
        disconnect_db(connection)
    except :
        print("Failed to list people")

