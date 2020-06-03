import sqlite3
from models import User, Post, Topic, Category
conn = sqlite3.connect('blog.db')
# cursor_connect = conn.cursor()
conn.execute("DROP TABLE user")
conn.execute('''CREATE TABLE USER
         (ID INT PRIMARY KEY     NOT NULL,
         EMAIL           TEXT    NOT NULL,
         PASSWORD            INT     NOT NULL,
         BIRTHDATE        TEXT);
         ''')

conn.execute('''CREATE TABLE POST
         (ID INT PRIMARY KEY     NOT NULL,
         LABEL           TEXT    NOT NULL,
         );
         ''')


user_1 = User(id=1, password=3030, email="tryingthis@ymail.com",  birthdate="12th January 1980")
post_1 = Category(id=1, label='red')

conn.execute("INSERT INTO USER (ID,EMAIL,PASSWORD,BIRTHDATE) \
      VALUES ('user_1.id','user_1.email' , 'user_1.password', 'user_1.birthdate')")

conn.execute("INSERT INTO POST (ID,LABEL) \
      VALUES ('post_1.id','post_1.email' )")
conn.commit()
conn.commit()
conn.close()
