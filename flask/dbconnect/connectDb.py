import mysql.connector
myDb = mysql.connector.connect(
    host="127.0.0.1", user="root", passwd="123456", database="sql_store")

myCursor = myDb.cursor()

# selectCommand = "SELECT first_name, last_name FROM orders o JOIN customers c ON o.customer_id = c.customer_id"
# selectCommand = "CREATE TABLE appUsers (id int, username text, password text)"
# myCursor.execute(selectCommand)
# result = myCursor.fetchall()
# for row in result:
#     print(f"{row[0]} {row[1]}")

# appUser = (1, "Venkata", "abc")
appUsers = [(2, "Kamesh", "abc"), (3, "Dhoni", "abc"), (4, "Mahi", "abc")]
insertQuery = "INSERT INTO appUsers VALUES (%s, %s, %s)"
myCursor.executemany(insertQuery, appUsers)

myDb.commit()
myDb.close()
