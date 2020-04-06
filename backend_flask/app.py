from flask import Flask, render_template, request, jsonify
import json
import requests
import sqlite3
import string
import datetime
import csv
import random
app = Flask(__name__)

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
if __name__ == '__main__':
    app.run()