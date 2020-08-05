print("Please pick a number between 1~31 and remember it.")
Z = input("Ready ? type something continue : ")
A = ['1','3','5','7','9','11','13','15','17','19','21','23','25','27','29','31']
B = ['2','3','6','7','10','11','14','15','18','19','22','23','26','27','30','31']
C = ['4','5','6','7','12','13','14','15','20','21','22','23','28','29','30','31']
D = ['8','9','10','11','12','13','14','15','24','25','26','27','28','29','30','31']
E = ['16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
L = [A,B,C,D,E]
q = []
ans = 0
I = 1
i = 1
while I == 1:
    for x in range(4):
        print(L[x])
        Z = input("Is the list has the number you pick? If yes enter '1' , If not enter '0' : ")
        while i == 1:
            if Z != '1' and Z != '0':
                print("Wrong type , try again")
                Z = input("Is the list has the number you pick? If yes enter '1' , If not enter '0' : ")
            else :
                q.append(int(Z))
                i = 0
    for x in range(4):
        if int(q[x]) == 1:
            ans = ans + int(L[x][0])
    print("I 'guess your number is : ",ans)
    z = input("Play again? If yes enter '1' ,If not enter something end : ")
    if z == 1:
        I = 1
    else :
        I = 0