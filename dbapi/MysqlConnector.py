import mysql.connector

class MySQLConnector:
    def __init__(self, host, username, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT 1")
        result = self.cursor.fetchone()
        print(result)

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def select_query(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def close_connection(self):
        self.cursor.close()
        self.conn.close()