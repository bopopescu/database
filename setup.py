import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.db_conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        self.db_connect = self.db_conn.cursor()

    def create_database(self):
        query = "CREATE DATABASE " + self.database
        self.db_connect.execute(query)

    def connect_db(self):
        self.db_conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        self.db_connect = self.db_conn.cursor()


    def select(self, table_name, column_name, condition):
        query = "SELECT "
        query += column_name + " " if column_name else "* "
        if condition:
            query += "FROM " + table_name + " WHERE " + condition
            print(query)
            self.db_connect.execute(query)
            return self.db_connect.fetchall()

        else:
            query += "FROM " + table_name
            print(query)
            self.db_connect.execute(query)
            return self.db_connect.fetchall()


    def insert(self, table_name, values, column_name):
        query = "INSERT INTO " + table_name + ' (' + ",".join(column_name) + ') ' + \
                "VALUES " + '(' + ",".join(values) + ');'
        print(query)
        self.db_conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password,
                                               database=self.database)
        self.db_connect = self.db_conn.cursor()
        self.db_connect.execute(query)
        self.db_conn.commit()

    def update(self,table_name, column_name, value, condition):
        query = "UPDATE " + table_name + " SET " + column_name + '=' + value
        if condition:
            query+= " "+ condition
            print(query)
            self.db_connect.execute(query)
            self.db_conn.commit()
        else:
            print(query)
            self.db_connect.execute(query)
            self.db_conn.commit()
