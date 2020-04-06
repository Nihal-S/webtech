from django.shortcuts import render
from django.http import HttpResponse
import csv
import random

def generate_questions(class_q):
    with open('questions/final_dataset.csv', mode='r') as csv_file:
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
        return class1[random.randint(0,len(class1)-1)]
    if(class_q == 2):
        return class2[random.randint(0,len(class2)-1)]
    if(class_q == 3):
        return class3[random.randint(0,len(class3)-1)]
    if(class_q == 4):
        return class4[random.randint(0,len(class4)-1)]
    if(class_q == 5):
        return class5[random.randint(0,len(class5)-1)]
    if(class_q == 6):
        return class6[random.randint(0,len(class6)-1)]
    if(class_q == 7):
        return class7[random.randint(0,len(class7)-1)]
    if(class_q == 8):
        return class8[random.randint(0,len(class8)-1)]
    if(class_q == 9):
        return class9[random.randint(0,len(class9)-1)]

def display_question(request):
    difficulty = random.randint(1,9)
    question = generate_questions(difficulty)
    return render(request,"question.html",{"question" : question[1]})
    # return HttpResponse("hello from questions") 
