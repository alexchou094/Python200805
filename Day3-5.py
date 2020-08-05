i = 1
while i == 1:
    print("---------------------")
    print("1 . addition")
    print("2 . subtraction")
    print("3 . multiplication")
    print("4 . division")
    print("5 . exit")
    p = input("What do you want to do next : ")
    if p == '1':
        a1 = input("number 1 : ")
        a2 = input("number 2 : ")
        print("The outcome of calculation : ")
        print(a1,"+",a2,"=",float(a1)+float(a2))
    if p == '2':
        a1 = input("number 1 : ")
        a2 = input("number 2 : ")
        print("The outcome of calculation : ")
        print(a1,"-",a2,"=",float(a1)-float(a2))    
    if p == '3':
        a1 = input("number 1 : ")
        a2 = input("number 2 : ")
        print("The outcome of calculation : ")
        print(a1,"x",a2,"=",float(a1)*float(a2))
    if p == '4':
        a1 = input("number 1 : ")
        a2 = input("number 2 : ")
        print("The outcome of calculation : ")
        print(a1,"/",a2,"=",float(a1)/float(a2))
    if p == '5':
        i = 0