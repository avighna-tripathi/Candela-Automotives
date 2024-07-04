import mysql.connector as mycon
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print("************************************************  WELCOME TO THE STORE  *******************************************")
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
def place_order():
    print("***********************************************************************************************************************")
    print()
    a1=int(input("Enter the budget of the current purchase ($):"))
    print()
    obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
    cur1=obj1.cursor()
    cur1.execute('SELECT DISTINCT MATERIALS FROM STORE;')
    print("THE ORDERABLE ITEMS ARE AS FOLLOWS :")
    print()
    i=0
    items=[]
    while True:
        i=i+1
        a2=cur1.fetchone()
        if a2==None:
            break
        items+=a2
        print(i,'. ',a2[0],sep='')
    print()
    obj1.close()
    a3=[]
    l=0
    total_price=0
    iii=()
    qqq=()
    quantity=()
    while True:
        l=l+1
        print("    PLACE ORDER FOR MATERIAL",l,':')
        a4=input('        Enter the material to be ordered:')
        if a4 not in items:
            print()
            print("No such item is present in the orderable items :(")
            print("                              Please try again !!!")
            break
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT QUALITY_GOOD,NET_PRICE FROM STORE WHERE MATERIALS='%s'"%(a4,))
        m=0
        while True:
            m+=1
            dat=cur1.fetchone()
            if dat==None:
                break
            print(m,'Quality:',dat[0],"    Price:",dat[1])
        a5=input("        Enter quality of good as budget allows (EXCELLENT/GOOD/SATISFACTORY) :")
        while a5 not in ('EXCELLENT','GOOD','SATISFACTORY','good','excellent','satisfactory','Good','Satisfactory','Excellent'):
            a5=input("        Enter legible quality (EXCELLENT/GOOD/SATISFACTORY) :")
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT NET_PRICE FROM STORE WHERE MATERIALS='%s' AND QUALITY_GOOD='%s'"%(a4,a5))
        F=cur1.fetchall()
        obj1.close()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT UNIT_PURCHASE FROM STORE WHERE MATERIALS='%s' AND QUALITY_GOOD='%s'"%(a4,a5))
        dta=cur1.fetchall()
        obj1.close()
        print("        Enter the quantity of ",a5,' ',a4,' ',"(in ",dta[0][0],")",sep='',end=':')
        a6=int(input())
        total_price=total_price+(F[0][0]*a6)
        iii=iii+(a4,)
        qqq=qqq+(a5,)
        quantity=quantity+(a6,)
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("UPDATE STOCKS_STORE SET QUANTITY=QUANTITY+{} WHERE MATERIALS='{}' AND QUALITY='{}'".format(a6,a4,a5))
        obj1.commit()
        f=input("Do you want to continue shopping (yes/no) :")
        if f in ('yes','YES','Yes','y','Y'):
            continue
        elif f in ('no','NO','No','n','N'):
            break
        else:
            print("             ******************** WRONG INPUT ********************")
            break
    x=0
    while x<len(iii):
        print()
        print("PRODUCT :",iii[x],"        QUALITY :",qqq[x],"         QUANTITY :",quantity[x])
        x=x+1
    print("Total cost price : ",total_price)
    fj=float(input("Enter the time of delivery (in days) :"))
    if fj<1:
        print()
        print("Since the time of delivery is less than a day,additional charges of 5000$ is applied on delivery...!!")
        print()
        total_price=total_price+5000
    if total_price>a1:
        print("TOTAL amount is more than the shopping budget  by",total_price-a1,"$ !!!")
        print("Searching for loan amounts....")
        print(".")
        print(".")
        print(".")
        import random
        o=random.randint(1,6)
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT NAME FROM INVESTORS')
        do=cur1.fetchall()
        obj1.close()
        print("Debt of",total_price-a1,"$ successfully approved from",do[o][0],"at 12% interest rate.")
    print()
    if fj>1:
        print("ORDER SUCCESSFULLY PLACED AND WILL BE DELIVERED WITHIN",fj,"DAYS   ^_^ !!!")
        print()
    elif fj<1:
        print("ORDER SUCCESSFULLY PLACED AND WILL BE DELIVERED WITHIN",fj,"DAYS or",fj*24,"HOURS  ^_^ !!!")
        print()
def use_goods():
    print("***********************************************************************************************************************")
    while True:
        print()
        print("THE PRODUCT AVAILABLE ARE :")
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT DISTINCT MATERIALS FROM STOCKS_STORE')
        items=[]
        while True:
            a=cur1.fetchone()
            if a==None:
                break
            print(a[0])
            items.append(a[0])
            items.append(a[0].upper())
            items.append(a[0].lower())
            print()
        obj1.close()
        s=input('Enter the products you want to use in manufacturing with comma separation and end.For eg: Leather,Glass, :')
        jj=[]
        p=''
        for i in s:
            if i==',':
                jj.append(p)
                p=''
                continue
            p=p+i
        s=jj
        prolist=[]
        for i in s:
            if i in items:
                print()
                print(i.upper(),"is in stock.")
                print()
                print("Enter the quality of",i,"(EXCELLENT/ GOOD/ SATISFACTORY) :")
                qual=input()
                while qual not in ('EXCELLENT','GOOD','SATISFACTORY','good','excellent','satisfactory','Good','Satisfactory','Excellent'):
                    qual=input("        Enter legible quality (EXCELLENT/GOOD/SATISFACTORY) :")
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute("SELECT MATERIALS,QUALITY,UNIT_MEASURE FROM STOCKS_STORE WHERE MATERIALS='%s' AND QUALITY='%s'"%(i,qual))
                datar=cur1.fetchall()
                obj1.close()
                print("Enter the quantity of",i,"to be ordered :",end='')
                quan=int(input())
                v1,v2,v3=datar[0]
                f1=(v1,v2,v3,quan)
                datar=f1
                prolist.append(datar)
            else:
                print()
                print(i,"is not among the orderable items..... ")
                print()
                print("AUTOCANCELLATION OF THE ORDER OF",i)
        print()
        print("*************************")
        print()
        print("THE FINAL ORDER LIST IS :")
        print()
        for i in prolist:
            print("MATERIAL :",i[0])
            print("QUALITY :",i[1])
            print("QUANTITY :",i[3],i[2])
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT QUANTITY FROM STOCKS_STORE WHERE MATERIALS='%s' AND QUALITY='%s'"%(i[0],i[1]))
            act_quan=cur1.fetchall()
            obj1.close()
            if i[3]>act_quan[0][0]:
                ov=i[3]-act_quan[0][0]
                print("There was a shortage of",i[1],"quality",i[0],"which has been fixed by direct order from company !!!")
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute("update stocks_store set quantity=quantity+cri_min+%s where materials='%s' and quality='%s'"%(ov,i[0],i[1]))
                obj1.commit()
                obj1.close()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("update stocks_store set quantity=quantity-%s where materials='%s' and quality='%s'"%(i[3],i[0],i[1]))
            obj1.commit()
            obj1.close()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("update manufacturing_stocks set stock=stock+%s where materials='%s' and quality='%s'"%(i[3],i[0],i[1]))
            obj1.commit()
            obj1.close()
            print()
        print("                                               ****** ORDER SUCCESSFUL, GOODS TRANDFERED TO MANUFACTURING DEPARTMENT ******")
        print()
        fk=input("Do You Want To Continue Tranfering to Manufacting (yes/no) :")
        if fk=='yes':
            continue
        elif fk=='no':
            break
        else:
            print("    WRONG INPUT")
            print()
            print("Implicit transfer to the main menu......")
            print()
def display_stock():
    print()    
    print("******************************************************************************************************************")
    print()
    print("1. To display the stock details of every product")
    print("2. To display the stock details of a specific product")
    print()
    d=input("Enter Your Choice (1-2) :")
    print()
    if d=='1':
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT MATERIALS,QUALITY,QUANTITY,UNIT_MEASURE FROM STOCKS_STORE')
        while True:
            ff=cur1.fetchone()
            if ff==None:
                break
            print("   Product :",ff[0])
            print("   Quality :",ff[1])
            print("   Stock_available :",ff[2],ff[3])
            print()
        obj1.close()
    elif d=='2':
        while True:
            print()
            ap=input("Enter the product you want to search :")
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute('SELECT DISTINCT MATERIALS FROM STOCKS_STORE')
            items=[]
            while True:
                a=cur1.fetchone()
                if a==None:
                    break
                items.append(a[0])
                items.append(a[0].upper())
                items.append(a[0].lower())
                print()
            obj1.close()
            if ap in items:
                pass
            else:
                print("   **********  PRODUCT NOT IN CANDELA STORE  *********")
                print()
                print("     **************   AutoCancellation Of Requet   **********")
                print()
                break
            ap=ap.capitalize()
            qq=input("Enter the quality of product you want to search (EXCELLENT/GOOD/SATISFACTORY) :")
            while qq not in ('EXCELLENT','GOOD','SATISFACTORY','good','excellent','satisfactory','Good','Satisfactory','Excellent'):
                qq=input("        Enter legible quality (EXCELLENT/GOOD/SATISFACTORY) :")
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute('SELECT MATERIALS,QUALITY,QUANTITY,UNIT_MEASURE FROM STOCKS_STORE')
            fff=cur1.fetchall()
            for i in fff:
                if i[0]==ap and i[1]==qq:
                    print()
                    print("   Product :",i[0])
                    print("   Quality :",i[1])
                    print("   Stock_available :",i[2],i[3])
                    print()
            obj1.close()
            k=input("Do you want to search for more goods? (yes/no) :")
            if k=='yes':
                continue
            elif k=='no':
                break
            else:
                print("    WRONG INPUT")
                print()
                print("Implicit transfer to the main menu......")
                print()
while True:
    print("1. TO PLACE ORDER OF GOODS")
    print("2. TO USE THE GOODS FOR MANUFACTURING")
    print("3. TO DISPLAY THE CURRENT STOCK.")
    print("4. EXIT")
    print()
    a=input("Enter your choice (1-5) :")
    if a=='1':
        place_order()
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print()
    elif a=='2':
        use_goods()
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print()
    elif a=='3':
        display_stock()
    elif a=='4':
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print()
        print("                  **************************** THANK YOU FOR USING THE STORE *******************************")
        print()
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")     
        break
    else:
        print()
        print("                                                              **************** WRONG INPUT *****************")
        print()
        print("                                                 ********************* PLEASE TRY AGAIN ********************")
        continue
