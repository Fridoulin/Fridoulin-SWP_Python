import mysql.connector


def connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NicerSpeck#",
        database="RockPaperScissors"
    )
    return conn


def database(choice, score):
    conn = connect()
    stmt = conn.cursor()
    stmt.execute("use RockPaperScissors")
    stmt.execute("CREATE TABLE if not exists symbol (choice VARCHAR(20), score Varchar(20));")
    query = "INSERT INTO symbol (choice, score) VALUES (%s, %s)"
    stmt.execute(query, (choice, score))
    conn.commit()
    stmt.close()
    conn.close()
