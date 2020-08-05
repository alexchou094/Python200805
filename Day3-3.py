nP = input("how many student in your class : ")
nP = int(nP)
name = []
grade = []
total  = 0
for i in range(nP):
    N = input("Please enter students' name : ")
    name.append(N)
    G = input("Please enter the student's grade : ")
    grade.append(G)
       
def average(nP):
    total = 0
    for i in range(nP):
        total = total + int(grade[i])    
    a = total /nP
    return a
        
def highestscore(nP):
    H = 0
    for i in range(nP):
        if int(grade[i]) > H:
            H = int(grade[i])
    return H

def highestperson(nP):
    H = 0
    Hp = 0
    for i in range(nP):
        if int(grade[i]) > H:
            Hp = str(name[i])
    return Hp

def lowestscore(nP):
    L = 101
    for i in range(nP):
        if int(grade[i]) < L:
            L = int(grade[i])
    return L

def lowestperson(nP):
    L = 101
    Lp = 0
    for i in range(nP):
        if int(grade[i]) < L:
            Lp = str(name[i])  
    return Lp

avg = average(nP)
H = highestscore(nP)
Hp = highestperson(nP)
L = lowestscore(nP)
Lp = lowestperson(nP)

print("The average is ",avg)
print("The highest person is ",Hp," : ",H,"points")
print("The lowest person is ",Lp," : ",L,"points")
