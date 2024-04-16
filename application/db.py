import pymysql

DB_HOST = 'localhost'
DB_PORT = 3306
DB_USER = 'root'
DB_PASS = ''
DB_NAME = 'practice_flask'

db = pymysql.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS)

cursor = db.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
cursor.execute(f"USE {DB_NAME}")

cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("""
    CREATE TABLE users (
        userID INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    )
""")

cursor.close()
db.close()
