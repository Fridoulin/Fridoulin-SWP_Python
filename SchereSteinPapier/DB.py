import mysql.connector
def connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NicerSpeck#"
    )

def database():
    stmt = mydb.cursor()
    stmt.execute("create database if not exists RockPaperScissors;")
    stmt.execute("use RockPaperScissors")
    stmt.execute("CREATE TABLE if not exists customers (name VARCHAR(255), address VARCHAR(255));")
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    stmt.execute(sql, val)
    mydb.commit()
    print(stmt.rowcount, "record inserted.")
    stmt.execute("SELECT * FROM customers")
    myresult = stmt.fetchone()
    print(myresult)
