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

def select():
    conn = connect()
    stmt = conn.cursor()
    stmt.execute('select count(choice) as "Rock" from symbol where choice = "rock";')
    rock = stmt.fetchall()
    stmt.execute('select count(choice) as "Paper" from symbol where choice = "paper";')
    paper = stmt.fetchall()
    stmt.execute('select count(choice) as "Scissors" from symbol where choice = "scissors";')
    scissors = stmt.fetchall()
    stmt.execute('select count(choice) as "Lizard" from symbol where choice = "lizard";')
    lizard = stmt.fetchall()
    stmt.execute('select count(choice) as "Spock" from symbol where choice = "spock";')
    spock = stmt.fetchall()
    print("Rock", rock,"    Paper", paper,"   Scissors", scissors,"   Lizard", lizard,"   Spock", spock)
    stmt.close()
    conn.close()
