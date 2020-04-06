import csv
import random

# random.seed(1)

with open('final_dataset.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
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

# print(len(class1))
# print(len(class2))
# print(len(class3))
# print(len(class4))
# print(len(class5))
# print(len(class6))
# print(len(class7))
# print(len(class8))
# print(len(class9))

# dataset[random.randint(0,len(dataset))]

def generate_question(class_q):
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

difficulty = random.randint(1,9)

for i in range(10):
    selected = generate_question(difficulty)
    print(selected[1])
    ans = input()
    print(selected[2])
    print(difficulty)
    if(ans == selected[2]):
        difficulty += 1
        if (difficulty == 10):
            difficulty = random.randint(7,9)
    else:
        difficulty -= 1
        if (difficulty == 0):
            difficulty = random.randint(1,2)