print("歡迎進入系統")
d = {}
while True:
    print("1. 新增詞彙")
    print("2. 列出所有單字")
    print("3. 英翻中")
    print("4. 中翻英")
    print("5. 測驗學習成果")
    print("6. 離開")
    x = input("選擇功能 : ")
    if x == '1':
        while True:            
            addv = input("請輸入要新增的單字(按0跳出) : ")
            if addv == '0':
                break           
            else:
                addc = input("請輸入該單字的解釋 : ")
                d[ addv ] = addc
    if x == '2':
        for i in d:
            print(i,"是",d[i])   
    if x == '3':
        while True:
            inqv = input("請輸入要查詢的單字(按0退出) : ")
            if inqv == '0':
                break
            elif inqv in d:
                inqc = d[inqv]       
                print(inqv,"的解釋是",inqc)
            else :
                print("查無此字")
    if x == '4':
        while True:
            y = input("請輸入要查詢的中文(按0退出) : ")
            for voc,chi in d.items():
                if y == '0':
                   break
                elif y == chi:
                   print("這個字是",voc)
                else:
                   print("查無此字")
    if x == '6':
        break
            
         
     

    
