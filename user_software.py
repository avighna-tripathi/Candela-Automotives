print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print("                ******************************* WELCOME TO THE USER INTERFACE *******************************")
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
import mysql.connector as mycon
def rate():
    print('''We respect the feedback you provide to Candela.The feedback given is registered and thus used to improve your
    further experiences.Please Do not use this section for fun :)''')
    print()
    print("5.Excellent (♥__♥)")
    print("4.Very Good (^_^)")
    print("3.Nice (0_0)")
    print("2.Not Bad (-_-)")
    print("1.Worst Experience ever (;_;)")
    print()
    c1=input("Enter your good name:")
    c2=input("Age:")
    c3=input("City you live in:")
    c4=input("Model purchased :")
    c5=input("How do you rate Candela's technology,design and comfort (1-5) :")
    c6=input("How do you rate Candela's customer and after purchase services (1-5) :")
    print()
    print("***********************************************************************************************************************")
    print("Thank You for giving your precious feedback to us, we have registered your view and will bring all the legible")
    print("developments to improve your further experience :)")
    print()
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
def user():
    print("**  Hi! This is Stacy, your artificial Candela Web assistant.  **")
    print()
    d1=input("Please enter your name so that we can continue :")
    print()
    if len(d1)==0:
        while True:
            d1=input("           PLEASE ENTER YOUR NAME:")
            if len(d1)!=0:
                break
    d11=d1[0].capitalize()
    print("**Ok ",d1," may I call you....",d11," !! Nice name huh!!  ^_^**",sep='')
    print()
    print("**So",d11,"In order to get more familiar with each other....I would like to ask some of your info :) **")
    print()
    d2=input("Please enter your age:")
    if len(d2)==0:
        while True:
            d2=input("           PLEASE ENTER YOUR AGE:")
            if len(d2)!=0:
                break
    d4=input("The city you live in:")
    if len(d4)==0:
        while True:
            d4=input("           PLEASE ENTER YOUR CITY:")
            if len(d4)!=0:
                break
    while True:
        print("************************************************************************************************************")
        print()
        print("**What do you want to do now: **")
        print()
        print("1. CHECK OUT THE CANDELA CATALOG.")
        print("2. KNOW WHERE WE STAND AT THE SHARE MARKET")
        print("3. KNOW OUR INVESTORS")
        print("4. KNOW YOUR NEAREST CANDELA SHOWROOMS")
        print("5. USE EMI CALCULATOR")
        print("6. RATE YOUR EXPIRIENCE WITH CANDELA")
        print("7. FREQUANTLY ASKED QUESTIONS")
        print("8. CALL INTO A CANDELA CARE")
        print("9. EXIT THE USER INTERFACE")
        print()
        d5=input("Your choice please (1-9) :")
        print()
        if d5=='1':
            print("=====================================================================================")
            print("CANDELA PROVIDES THE FOLLOWING CAR MODELS:")
            print()
            print("HATCHBACKS:  S,X,Y")
            print("SUVs                  :  M,C,D")
            print("SEDANS            :  T,Z     ")
            print("TRUCKS            :  F ")
            while True:
                print()
                f=input("Enter the name of the model you want to take info on (uppercase) :")
                if f=='S':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM S_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,":",f3)
                    obj3.close()
                elif f=='X':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM X_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,":",f3)
                    obj3.close()
                elif f=='Y':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM Y_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,":",f3)
                    obj3.close()
                elif f=='M':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM MEGA_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,':',f3)
                    obj3.close()
                elif f=='C':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM COULOMB_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,':',f3)
                    obj3.close()
                elif f=='D':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM DECA_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,':',f3)
                    obj3.close()
                elif f=='T':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM CYBERTRUCK_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,':',f3)
                    obj3.close()
                elif f=='Z':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM ZETAR_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,':',f3)
                    obj3.close()
                elif f=='F':
                    obj3=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                    cur3=obj3.cursor()
                    cur3.execute('SELECT * FROM SEMI_CATALOG')
                    while True:
                        f1=cur3.fetchone()
                        if f1==None:
                            break
                        f2,f3=f1
                        print(f2,':',f3)
                    obj3.close()
                f33=input("**Press enter for more catalogs,to quit enter any key(then enter)** :")
                if f33=='':
                    continue
                else:
                    break
        elif d5=='2':
            print("=====================================================================================")
            import random
            print()
            sp=['236$','521$','1024$','2056$','962$','3211$','1026$','765$']
            pp=['1%','2%','3%','4%','5%','6%','7%','8%','9%']
            spp=['↑','↓']
            sp1=sp[random.randint(0,7)]
            pp1=pp[random.randint(0,8)]
            spp1=spp[random.randint(0,1)]
            print("Currently Candela's shares lies at  {{ ",sp1," ",pp1,spp1," }}")
        elif d5=='3':
            print("=====================================================================================")
            obj4=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA');
            cur4=obj4.cursor()
            cur4.execute('SELECT * FROM INVESTORS')
            while True:
                g=cur4.fetchone()
                if g==None:
                    break
                g1,g2,g3,g4,g5=g
                print(g1,g2,',',g3,', invested',g4,' and',g5,'in debt')
            obj4.close()
        elif d5=='4':
            print("=====================================================================================")
            print("CANDELA HAS ITS SHOWROOMS IN:")
            print()
            obj5=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA');
            cur5=obj5.cursor()
            cur5.execute('SELECT * FROM SHOWROOMS')
            while True:
                h=cur5.fetchone()
                if h==None:
                    break
                h1,h2,h3,h4=h
                print(h1,' ',h2," at",h3,'mobile no: ',h4)
            obj5.close()
        elif d5=='5':
            o1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=o1.cursor()
            print("=====================================================================================")
            e4=tuple(input("Enter car model name (uppercase) :"))
            cur1.execute("SELECT BASE_PRICE FROM CATALOG WHERE MODEL='%s'"%(e4))
            e1=int(cur1.fetchall()[0][0])
            cur1.execute("SELECT EMI_INTEREST FROM CATALOG WHERE MODEL='%s'"%(e4))
            e2=(int(cur1.fetchall()[0][0]))/1200
            e3=int(input("Enter the number of months:"))
            EMI=e1 * e2 * (1+e2)**e3/((1+e2)**e3-1)
            print("Your EMI comes to be ",int(EMI),"$ per month with loan amout: ",e1,"$ at ",1200*e2,"% per annum.",sep='')
            o1.close()
        elif d5=='6':
            rate()
        elif d5=='7':
            while True:
                print()
                print("1. Order")
                print("2. Payment")
                print("3. Insurance")
                print("4. Charging solutions")
                print("5. Exit")
                print()
                ch=input('Enter the subect on which you want the solution (1-5) :')
                print()
                if ch=='1':
                    print()
                    print("""HOW DO I ORDER A CANDELA?
Visit our Design Studio to explore our latest options and place your order.
The purchase price and estimated delivery date will change based on your configuration.

CAN I REQUEST A CANDELA DRIVE?
Yes, you can request for a test drive.
Please note that drivers must be a minimum of 27 years of age and not exceeding 65 years of age,
hold a full driving license with over 2 years of driving experience.
Insurance conditions relating to your specific status must be reviewed and accepted prior to the test drive.""")
                    print()
                elif ch=='2':
                    print()
                    print('''WHAT ARE THE ACCEPTED METHODS OF PAYMENT?
You can submit your final payment via bank transfer.

HOW MUCH DO I OWE BEFORE DELIVERY?
We require the full balance to be paid in full prior to delivery.''')
                    print()
                elif ch=='3':
                    print()
                    print('''HOW CAN I APPLY FOR CAR INSURANCE?
Liberty Insurance is our preferred insurance partner in Singapore.
If you would want to make an insurance inquiry, please contact Liberty Insurance at:
1800-PREMIUM (773 6486) or you can also send an email to candela.sg@libertyinsurance.com.sg.''')
                    print()
                elif ch=='4':
                    print()
                    print('''HOW DO I INSTALL HOME CHARGING STATION ?
For customers with access to private garage:
To be made available for purchase closer to launch, the Candela Wall Connector is recommended for convenient charging at home.
We recommend that you hire Candela Certified Installer for the best experience and workmanship.''')
                    print()
                elif ch=='5':
                    break
                else:
                    print("                   *********** WRONG INPUT **********")
                    print()
                    print("            ************ PLEASE TRY AGAIN ***********")
                    print()
                    continue
        elif d5=='8':
            print()
            print("YOU CAN CALL TO ANY OF THE FOLLOWING NUMBERS AS PER YOUR RESPECTIVE CITIES :")
            print()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute('SELECT * FROM SHOWROOMS')
            city=[]
            items=[]
            while True:
                O=cur1.fetchone()
                if O==None:
                    break
                items.append(O)
                city.append(O[1])
            a=input("Which city are you from (uppercase):")
            gm=a.upper()
            if gm not in city:
                print()
                print("SORRY....CANDELA ISN'T CURRENTLY PRESENT IN YOUR CITY (;__;)...")
                print()
                print("Cities in which Candela help is available are:")
                for i in city:
                    print(i,end=' ,')
                print()
                continue
            for i in items:
                if i[1]==a:
                    print("    Candela Center :",i[2])
                    print("    Helpline number :",i[3])
        elif d5=='9':
            print()
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print()
            print(" ****************************  THANK YOU FOR USING THE USER INTERFACE *****************************")
            print()
            print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            break
        else:
            print("                                    **************************************** Wrong Input   o_o  ***********************************")
            print()
            print("                                    *************************************** PLEASE TRY AGAIN  *********************************")
            print()
            continue 
user()
