while True:
    ps=input("Enter new password (max 8) :  ")
    if len(ps)>8:
        print("Password more than 8 please try again")
    else :
        i = 0
        while i<=3:
            psn=input("Enter password : ")
            if psn!=ps :
                print("Password not correct!!!")
                i=i+1
                if i>=3:
                    break
            elif ps==psn :
                print("Password correct")
                i=0
                ps=input("Please setup new password (max 8:)")
    break
