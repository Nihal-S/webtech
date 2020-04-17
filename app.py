from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import requests
import sqlite3
import string
import datetime
import csv
import random
import yagmail
import re 
import matplotlib.pyplot as plt 
app = Flask(__name__)
CORS(app)

def plot_graph(d):
    x = []
    y = []
    for i in d:
        y.append(i["marks"]*i["difficulty"])
        x.append(i["testid"])

    plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3, 
            marker='o', markerfacecolor='blue', markersize=12)  
    plt.ylim(0,900) 
    plt.xlim(0,max(x)) 
    plt.xlabel('Testid') 
    plt.ylabel('Score * Difficulty')  
    plt.title('Graph') 
    plt.savefig("test.png",dpi = 1000)

def check_email(email):  
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$' 
    if(re.search(regex,email)):  
        return True
    else:  
        return False

def send_json(data_as_list):
    dictionary = {}
    dictionary["title"] = data_as_list[0]
    dictionary["question"] = data_as_list[1]
    dictionary["answer"] = data_as_list[2]
    dictionary["class"] = data_as_list[-1]
    return dictionary

@app.route('/getquestion', methods=['POST'])
def generate_question():
    class_q = request.json['class_q']
    class_q = int(class_q)
    print(class_q)
    with open('final_dataset.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        dataset = []
        for row in csv_reader:
            dataset.append(row)
    class1 = []
    class2 = []
    class3 = []
    class4 = []
    class5 = []
    class6 = []
    class7 = []
    class8 = []
    class9 = []
    for row in dataset:
        if(row[3] == "easy" and row[4] == "easy"):
            row.append(1)
            class1.append(row)
        if(row[3] == "easy" and row[4] == "medium"):
            row.append(2)
            class2.append(row)
        if(row[3] == "easy" and row[4] == "hard"):
            row.append(3)
            class3.append(row)
        if(row[3] == "medium" and row[4] == "easy"):
            row.append(4)
            class4.append(row)
        if(row[3] == "medium" and row[4] == "medium"):
            row.append(5)
            class5.append(row)
        if(row[3] == "medium" and row[4] == "hard"):
            row.append(6)
            class6.append(row)
        if(row[3] == "hard" and row[4] == "easy"):
            row.append(7)
            class7.append(row)
        if(row[3] == "hard" and row[4] == "medium"):
            row.append(8)
            class8.append(row)
        if(row[3] == "hard" and row[4] == "hard"):
            row.append(9)
            class9.append(row)
    if(class_q == 1):
        return jsonify(send_json(class1[random.randint(0,len(class1)-1)]))
    if(class_q == 2):
        return jsonify(send_json(class2[random.randint(0,len(class2)-1)]))
    if(class_q == 3):
        return jsonify(send_json(class3[random.randint(0,len(class3)-1)]))
    if(class_q == 4):
        return jsonify(send_json(class4[random.randint(0,len(class4)-1)]))
    if(class_q == 5):
        return jsonify(send_json(class5[random.randint(0,len(class5)-1)]))
    if(class_q == 6):
        return jsonify(send_json(class6[random.randint(0,len(class6)-1)]))
    if(class_q == 7):
        return jsonify(send_json(class7[random.randint(0,len(class7)-1)]))
    if(class_q == 8):
        return jsonify(send_json(class8[random.randint(0,len(class8)-1)]))
    if(class_q == 9):
        return jsonify(send_json(class9[random.randint(0,len(class9)-1)]))

@app.route('/getallusers', methods=['POST'])
def getallusers():
    conn = sqlite3.connect('adaptive_test.db')
    c = conn.cursor()
    query = "SELECT username FROM users"
    c.execute(query)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return json.dumps(rows)

@app.route('/getallemails', methods=['POST'])
def getallemails():
    conn = sqlite3.connect('adaptive_test.db')
    c = conn.cursor()
    query = "SELECT email FROM users"
    c.execute(query)
    rows = c.fetchall()
    conn.commit()
    conn.close()
    return json.dumps(rows)

@app.route('/login', methods=['POST'])
def login():
    print(1)
    username = request.json["username"]
    password = request.json["password"]
    print(username)
    print(password)
    names = requests.post("http://127.0.0.1:5000/getallusers",json={})
    names = names.json()
    l = []
    for i in names:
        l.append(i[0])
    names = l
    if(username in names):
        conn = sqlite3.connect("adaptive_test.db")
        c = conn.cursor()
        query = "SELECT username,password FROM users WHERE username= '"+username+"'"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
    else:
        return jsonify(),400
    # print(rows[0][0],rows[0][1])
    if(rows[0][0] == username and rows[0][1] == password):
        return jsonify(),201
    else:
        return jsonify(),400


@app.route('/sign_up', methods=['POST'])
def sign_up():
    username = request.json["username"]
    password = request.json["password"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    names = requests.post("http://127.0.0.1:5000/getallusers",json={})
    names = names.json()
    l = []
    for i in names:
        l.append(i[0])
    names = l
    emails = requests.post("http://127.0.0.1:5000/getallemails",json={})
    emails = emails.json()
    l = []
    for i in emails:
        l.append(i[0])
    emails = l
    print(emails)
    print(names)
    if (email not in emails and username not in names):
        conn = sqlite3.connect("adaptive_test.db")
        c = conn.cursor()
        print(username)
        print(password)
        print(firstname)
        print(lastname)
        print(email)
        query = "INSERT INTO users(username,password,firstname,lastname,email) VALUES ('"+username+"','"+password+"','"+firstname+"','"+lastname+"','"+email+"')"
        c.execute(query)
        conn.commit()
        conn.close()
        return jsonify(),201
    else:
        return jsonify(),400


@app.route('/test_details', methods=['POST'])
def test_details():
    username = request.json["username"]
    marks = request.json["marks"]
    difficulty = request.json["difficulty"]
    print(username)
    print(marks)
    print(difficulty)
    names = requests.post("http://127.0.0.1:5000/getallusers",json={})
    names = names.json()
    l = []
    for i in names:
        l.append(i[0])
    names = l
    if(username in names):
        conn = sqlite3.connect("adaptive_test.db")
        c = conn.cursor()
        query = "INSERT INTO test(username,marks,difficulty) VALUES ('"+username+"','"+marks+"','"+difficulty+"')"
        c.execute(query)
        conn.commit()
        conn.close()    
        return jsonify(),201 
    else:
        return jsonify(),400 


@app.route('/individual_test_details', methods=['POST'])
def individual_test_details():
    username = request.json["username"]
    password = request.json["password"]
    names = requests.post("http://127.0.0.1:5000/getallusers",json={})
    names = names.json()
    l = []
    for i in names:
        l.append(i[0])
    names = l
    if(username in names):
        conn = sqlite3.connect("adaptive_test.db")
        c = conn.cursor()
        query = "SELECT username,password FROM users WHERE username='"+username+"'"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
    else:
        return jsonify(),400
    if(rows[0][0] == username and rows[0][1] == password):
        conn = sqlite3.connect("adaptive_test.db")
        c = conn.cursor()
        query = "SELECT testid,marks,difficulty FROM test WHERE username='"+username+"'"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        l1= []
        for i in rows:
            dictionary = {}
            dictionary["testid"] = i[0]
            dictionary["marks"] = i[1]
            dictionary["difficulty"] = i[2]
            l1.append(dictionary)
        plot_graph(l1)
        return jsonify(l1),201
    else:
        return jsonify(),400

@app.route('/forgotpassword', methods=['POST'])
def forgotpassword():
    #not working get touch up;
    username = request.json["username"]
    names = requests.post("http://127.0.0.1:5000/getallusers",json={})
    names = names.json()
    l = []
    for i in names:
        l.append(i[0])
    names = l
    if(username not in names):
        return jsonify(),400
    else:
        conn = sqlite3.connect("adaptive_test.db")
        c = conn.cursor()
        query = "SELECT password,email FROM users WHERE username='"+username+"'"
        c.execute(query)
        rows = c.fetchall()
        conn.commit()
        conn.close()
        sender_email = "testeradaptive@gmail.com"
        password = "K77vVqv7d6wQVNj"
        yag_smtp_connection = yagmail.SMTP( user=sender_email, password=password, host='smtp.gmail.com')
        subject = "YOUR PASSWORD FOR ADAPTIVE TESTING IS"
        contents = ['Password: '+rows[0][0]]
        yag_smtp_connection.send(rows[0][1],subject,contents)
        print("An email has been sent to the client")

        return jsonify({"email":rows[0][1]}),200

@app.route('/checkmail', methods=['POST'])
def check_mail():
    email = request.json["email"]
    print(email)
    if(check_email(email)):
        return jsonify(),200
    else:
        return jsonify(),400

@app.route('/checkusername', methods=['POST'])
def check_usn():
    username = request.json["username"]
    names = requests.post("http://127.0.0.1:5000/getallusers",json={})
    names = names.json()
    l = []
    for i in names:
        l.append(i[0])
    names = l
    if(username in names):
        return jsonify(),400
    else:
        return jsonify(),200

@app.route('/checkpassword', methods=['POST'])
def check_passwd():
    passwd = request.json["password"]
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pat = re.compile(reg) 
    mat = re.search(pat, passwd) 
    if mat: 
        return jsonify(),200 
    else: 
        return jsonify(),400

@app.route('/feedback', methods=['POST'])
def feedback():
    username = request.json["username"]
    feedback = request.json["feedback"]
    f = open("feedback.csv",'a')
    f.write(username+","+feedback+"\n")
    f.close()
    return jsonify(),201

@app.route('/chat', methods=['POST'])
def chat():
    username = request.json["username"]
    fchatter = open("chatter.txt",'a')
    fchat = open("chat.txt",'r')
    chatofone = fchat.read()
    fchatter.write(username+"\t")
    fchatter.write(chatofone)
    fchatter.write('\n')
    fchat.close()
    fchat = open("chat.txt",'w')
    fchat.close()
    fchatter.close()
    return jsonify(),201


if __name__ == '__main__':
    app.run(debug=True)