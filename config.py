from pymysql import cursors

DEBUG = True
PORT = 8000
HOST = "localhost"
MYSQL_CONFIG = {"host": "112.74.215.22",
                "port": 3306,
                "user": "",
                "password": "",
                "db": "contest",
                "charset": "utf8mb4",
                'cursorclass': cursors.DictCursor}
