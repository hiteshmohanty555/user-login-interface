import mysql.connector

connection = mysql.connector.connect(
        host='localhost', user='root', password='123456', port='3306')
cursor = connection.cursor()
insert_query="create database test_py"
cursor.execute(insert_query)
insert_query="use test_py"
cursor.execute(insert_query)
insert_query= "Create table users_2( sl_no int UNIQUE  AUTO_INCREMENT, firstname varchar(30) NOT NULL, lastname varchar(30) NOT NULL, email varchar(50) NOT NULL, age int NOT NULL, ph_no double PRIMARY KEY, d_o_r DATE NOT NULL, t_o_r TIME NOT NULL);"
cursor.execute(insert_query)
connection.commit()
connection.close()
