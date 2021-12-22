import mysql.connector
import requests

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
    rock = str(rock).replace('[(','').replace(',)]','')
    paper = str(paper).replace('[(','').replace(',)]','')
    scissors = str(scissors).replace('[(','').replace(',)]','')
    lizard = str(lizard).replace('[(','').replace(',)]','')
    spock = str(spock).replace('[(','').replace(',)]','')
    print("Rock: ", rock,"    Paper: ", paper,"   Scissors: ", scissors,"   Lizard: ", lizard,"   Spock: ", spock)

    print("sending test request")
    sendRequest("User",scissors,rock,paper,spock, lizard)
    code = sendRequest("User", 1, 2, 3, 4, 5)
    #print(code = " + str(code))
    print("Done")
    stmt.close()
    conn.close()



def sendRequest(username, voteScissors, voteRock, votePaper, voteSpock, voteLizard, apiIP = "http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl+= "?username=" + str(username) + "&voteScissors=" + str(voteScissors)
    reqUrl+= "&voteRock=" + str(voteRock) + "&votePaper=" + str(votePaper)
    reqUrl+= "&voteSpock=" + str(voteSpock) + "&voteLizard=" + str(voteLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode

def send_request(rock, paper, scissors, lizard, spock):

    return sendRequest("User", rock, paper, scissors, lizard, spock)
