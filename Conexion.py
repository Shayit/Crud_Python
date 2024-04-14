import mysql.connector
from mysql.connector import Error

BD = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001",
    database="usuarios"
)

cursor = BD.cursor()