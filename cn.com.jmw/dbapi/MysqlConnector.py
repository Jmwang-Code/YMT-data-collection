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

    # 测试连接
    def test_connection(self):
        self.cursor.execute("SELECT 1")
        result = self.cursor.fetchone()
        print(result)

    # `执行查询` 用于执行更新操作（插入、更新、删除）并提交更改。
    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    # `执行查询` 用于执行查询操作并返回结果行。
    def select_query(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    # 关闭连接
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
