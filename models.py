import mysql.connector
# mydb = mysql.connector.connect(host = "127.0.0.1", user='root', password= "")

from setup import Database


class User:
    def __init__(self, id, email='', password='', birthdate=''):
        self.id = id
        self.email = email
        self.password = password
        self.birthdate = birthdate
        self.db = Database(host="127.0.0.1", user='root', password="", database="Webapp")
        self.db.connect_db()

    def insert(self):
        try:
            self.db.insert("USERS", ("'"+self.email + "'", "'"+self.birthdate+"'", "'"+self.password+"'"),
                  ('email', 'birthdate', 'password'))

        except TypeError:
            print("Invalid data format")
        return True

    def update(self):
        self.db.update("USERS", 'password', "'oldpass'", 'WHERE id= 10')

    def find(self):
        records = self.db.select("USERS", "","id = " + str(self.id))
        for row in records:
            return User(row[3], row[0], row[2], row[1])

    def __repr__(self):
        return f"User('{self.email}','{self.password}','{self.birthdate}')"


class Category:
    def __init__(self, id, label):
        self.id = id
        self.label = label

    def __repr__(self):
        return f"Category('{self.id}', '{self.label}')"


class Topic:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return f"Topic('{self.id}', '{self.title}')"


class Post:
    def __init__(self, id, postdate, content):
        self.id = id
        self.postDate = postdate
        self.content = content

    def __repr__(self):
        return f"Post('{self.id}', '{self.postDate}','{self.content}')"


#user_1 = User(id=1, password=3030, email="tryingthis@ymail.com",  birthdate="12th January 1980")
#db = Database(host="127.0.0.1", user='root', password="", database="Webapp")
#db.create_database()
#db.connect_db()
#db.db_connect.execute("CREATE TABLE USERS (email VARCHAR(255), birthdate VARCHAR(255), password VARCHAR(255), id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#db.db_connect.execute("SHOW TABLES")
#for table in db.db_connect:
#    print(table)
#user = User(4)
#user = user.find()
#user = user.insert()

user_1 = User(id=7, password="test123", email="tryingthis@ymail.com",  birthdate="12th January 1980")
user = user_1.insert()


