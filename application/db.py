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

# drop tables
cursor.execute("DROP TABLE IF EXISTS users")
cursor.execute("DROP TABLE IF EXISTS user_types")

# create tables
cursor.execute("""
    CREATE TABLE user_types (
        userTypeID TINYINT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) UNIQUE NOT NULL
    ) ENGINE=InnoDB;
""")
cursor.execute("""
    CREATE TABLE users (
        userID INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL, 
        userTypeID TINYINT NOT NULL, 
        FOREIGN KEY (userTypeID) REFERENCES user_types (userTypeID)
    ) ENGINE=InnoDB;
""")

# insert necessary records
cursor.execute("""
    INSERT INTO user_types (`name`)
    VALUES 
        ('Administrator'),
        ('Personnel');
""")

# commit queries
db.commit()

# close
cursor.close()
db.close()
