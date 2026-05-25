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
    query = ' CREATE TABLE people IF NOT EXISTS (id INT PRIMARY KEY AUTO_INCREMENT , name VARCHAR(64) NOT NULL,gender BOOL NOT NULL,age int default(0),location VARCHAR(32));'
    try:
        connection=connect_db()
        cursor = connection.cursor()
        count=cursor.execute(query)
        if count == 0:
            print("Table created successfully")
        else:
            print("Table creation failed")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Table creation failed")


def create_table():
    query = ' CREATE TABLE people IF NOT EXISTS (id INT PRIMARY KEY AUTO_INCREMENT , name VARCHAR(64) NOT NULL,gender BOOL NOT NULL,age int default(0),location VARCHAR(32));'
    try:
        connection=connect_db()
        cursor = connection.cursor()
        count=cursor.execute(query)
        if count == 0:
            print("Table created successfully")
        else:
            print("Table creation failed")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Table creation failed")




create_table()