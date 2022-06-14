# importing required libraries
import mysql.connector

connection = mysql.connector.connect(
host ="localhost",
user ="admin",
passwd ="admin",
database='latihan_python',
)

with connection:
    with connection.cursor() as cursor:
        imel = 'admin@gmail.com'
        val = (imel)
        sql = "SELECT * FROM users WHERE ffcuser=%s"
        cursor.execute(sql, val)
        result = cursor.fetchone()
        if result == None:
            print('data tidak ditemukan')
        else:            
            print(result)