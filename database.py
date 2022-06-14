import pymysql

# Connect to the database
connection = pymysql.connect(
    host='localhost',
    user='admin',
    password='admin',
    database='latihan_python',
    port=3307,
    cursorclass=pymysql.cursors.DictCursor
)

