import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NicerSpeck#",
        database="RockPaperScissors"
    )
    return conn


def database(val):
    conn = connect()
    stmt = conn.cursor()
    stmt.execute("use RockPaperScissors")
    stmt.execute("CREATE TABLE if not exists symbol (choice VARCHAR(255));")
    query = "INSERT INTO symbol (choice) VALUES (%s)"
    stmt.execute(query, (val,))
    conn.commit()
    stmt.close()
    conn.close()
