import mysql.connector as mycon
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print("         ********************************* WELCOME TO THE HR INTERFACE **************************************")
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
def calendar():
    print()
    print("1. March - May")
    print("2. Jun - Aug")
    print("3. Sep - Nov")
    print("4. Dec - Feb")
    print()
    a=input("Enter the quater in which you want to design the activity calendar (1-4) :")
    print()
    if a=='1':
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        print()
        print("Choose the 9 activities to be done in this quater:")
        print()
        cur1.execute('SELECT * FROM ACTIVITY')
        while True:
            dat=cur1.fetchone()
            if dat==None:
                break
            print(dat[0],'.',dat[1])
        obj1.close()
        print()
        g=eval(input("Enter the activities you choose in order of occurence (1-11).For eg, (4,2,3,....) :"))
        print()
        date_mar=eval(input("Enter three dates of events of march in a list .For eg,[1,16,31] :"))
        while len(date_mar)>3:
            date_mar=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_apr=eval(input("Enter three dates of events of april in a list.For eg,[1,16,31] :"))
        while len(date_apr)>3:
            date_apr=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_may=eval(input("Enter three dates of events of may in a list.For eg,[1,16,31] :"))
        while len(date_may)>3:
            date_may=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        ff=date_mar+date_apr+date_may
        i=0
        while True:
            i+=1
            if i==10:
                break
            if i in (1,2,3):
                ff[i-1]=str(ff[i-1])+' March'
            if i in (4,5,6):
                ff[i-1]=str(ff[i-1])+' April' 
            if i in (7,8,9):
                ff[i-1]=str(ff[i-1])+' May'
        i=0
        while True:
            if i==9:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT NAME,NO_PEOPLE,DURATION FROM ACTIVITY WHERE SNO=%s"%(g[i]))
            da=cur1.fetchall()
            obj1.close()
            if i==10:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("INSERT INTO ONE_ACTIVITY VALUES({},'{}',{},'{}','{}')".format(i+1,da[0][0],da[0][1],da[0][2],ff[i]))
            obj1.commit()
            obj1.close()
            i+=1
        print()
        print("THE EVENT CALENDAR FOR MARCH-MAY IS :")
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT * FROM ONE_ACTIVITY")
        while True:
            hd=cur1.fetchone()
            if hd==None:
                break
            print(hd[0],".    Event name:",hd[1],"          ON:",hd[4])
        obj1.close()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("DELETE FROM ONE_ACTIVITY WHERE SNO>%s"%(0,))
        obj1.commit()
        obj1.close()
    elif a=='2':
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        print()
        print("Choose the 9 activities to be done in this quater:")
        print()
        cur1.execute('SELECT * FROM ACTIVITY')
        while True:
            dat=cur1.fetchone()
            if dat==None:
                break
            print(dat[0],'.',dat[1])
        obj1.close()
        print()
        g=eval(input("Enter the activities you choose in order of occurence (1-11).For eg, (4,2,3,....) :"))
        print()
        date_mar=eval(input("Enter three dates of events of june in a list.For eg,[1,16,31] :"))
        while len(date_mar)>3:
            date_mar=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_apr=eval(input("Enter three dates of events of july in a list.For eg,[1,16,31] :"))
        while len(date_apr)>3:
            date_apr=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_may=eval(input("Enter three dates of events of august in a list.For eg,[1,16,31] :"))
        while len(date_may)>3:
            date_may=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        ff=date_mar+date_apr+date_may
        i=0
        while True:
            i+=1
            if i==10:
                break
            if i in (1,2,3):
                ff[i-1]=str(ff[i-1])+' June'
            if i in (4,5,6):
                ff[i-1]=str(ff[i-1])+' July' 
            if i in (7,8,9):
                ff[i-1]=str(ff[i-1])+' August'
        i=0
        while True:
            if i==9:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT NAME,NO_PEOPLE,DURATION FROM ACTIVITY WHERE SNO=%s"%(g[i]))
            da=cur1.fetchall()
            obj1.close()
            if i==10:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("INSERT INTO TWO_ACTIVITY VALUES({},'{}',{},'{}','{}')".format(i,da[0][0],da[0][1],da[0][2],ff[i]))
            obj1.commit()
            obj1.close()
            i+=1
        print()
        print("THE EVENT CALENDAR FOR MARCH-MAY IS :")
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT * FROM ONE_ACTIVITY")
        while True:
            hd=cur1.fetchone()
            if hd==None:
                break
            print(hd[0],".    Event name:",hd[1],"          ON:",hd[4])
        obj1.close()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("DELETE FROM TWO_ACTIVITY WHERE SNO>%s"%(0,))
        obj1.commit()
        obj1.close()
    elif a=='3':
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        print()
        print("Choose the 9 activities to be done in this quater:")
        print()
        cur1.execute('SELECT * FROM ACTIVITY')
        while True:
            dat=cur1.fetchone()
            if dat==None:
                break
            print(dat[0],'.',dat[1])
        obj1.close()
        print()
        g=eval(input("Enter the activities you choose in order of occurence (1-11).For eg, (4,2,3,....) :"))
        print()
        date_mar=eval(input("Enter three dates of events of septemberin a list.For eg,[1,16,31] :"))
        while len(date_mar)>3:
            date_mar=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_apr=eval(input("Enter three dates of events of october in a list.For eg,[1,16,31] :"))
        while len(date_apr)>3:
            date_apr=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_may=eval(input("Enter three dates of events of november in a list.For eg,[1,16,31] :"))
        while len(date_may)>3:
            date_may=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        ff=date_mar+date_apr+date_may
        i=0
        while True:
            i+=1
            if i==10:
                break
            if i in (1,2,3):
                ff[i-1]=str(ff[i-1])+' September'
            if i in (4,5,6):
                ff[i-1]=str(ff[i-1])+' October' 
            if i in (7,8,9):
                ff[i-1]=str(ff[i-1])+' November'
        i=0
        while True:
            if i==9:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT NAME,NO_PEOPLE,DURATION FROM ACTIVITY WHERE SNO=%s"%(g[i]))
            da=cur1.fetchall()
            obj1.close()
            if i==10:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("INSERT INTO THREE_ACTIVITY VALUES({},'{}',{},'{}','{}')".format(i,da[0][0],da[0][1],da[0][2],ff[i]))
            obj1.commit()
            obj1.close()
            i+=1
        print()
        print("THE EVENT CALENDAR FOR MARCH-MAY IS :")
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT * FROM ONE_ACTIVITY")
        while True:
            hd=cur1.fetchone()
            if hd==None:
                break
            print(hd[0],".    Event name:",hd[1],"          ON:",hd[4])
        obj1.close()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("DELETE FROM THREE_ACTIVITY WHERE SNO>%s"%(0,))
        obj1.commit()
        obj1.close()
    elif a=='4':
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        print()
        print("Choose the 9 activities to be done in this quater:")
        print()
        cur1.execute('SELECT * FROM ACTIVITY')
        while True:
            dat=cur1.fetchone()
            if dat==None:
                break
            print(dat[0],'.',dat[1])
        obj1.close()
        print()
        g=eval(input("Enter the activities you choose in order of occurence (1-11).For eg, (4,2,3,....) :"))
        print()
        date_mar=eval(input("Enter three dates of events of december in a list.For eg,[1,16,31] :"))
        while len(date_mar)>3:
            date_mar=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_apr=eval(input("Enter three dates of events of january in a list.For eg,[1,16,31] :"))
        while len(date_apr)>3:
            date_apr=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        date_may=eval(input("Enter three dates of events of february in a list.For eg,[1,16,31] :"))
        while len(date_may)>3:
            date_may=eval(input("Please enter only three dates.For eg,[1,16,31] :"))
        ff=date_mar+date_apr+date_may
        i=0
        while True:
            i+=1
            if i==10:
                break
            if i in (1,2,3):
                ff[i-1]=str(ff[i-1])+' December'
            if i in (4,5,6):
                ff[i-1]=str(ff[i-1])+' January' 
            if i in (7,8,9):
                ff[i-1]=str(ff[i-1])+' February'
        i=0
        while True:
            if i==9:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT NAME,NO_PEOPLE,DURATION FROM ACTIVITY WHERE SNO=%s"%(g[i]))
            da=cur1.fetchall()
            obj1.close()
            if i==10:
                break
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("INSERT INTO ONE_ACTIVITY VALUES({},'{}',{},'{}','{}')".format(i,da[0][0],da[0][1],da[0][2],ff[i]))
            obj1.commit()
            obj1.close()
            i+=1
        print()
        print("THE EVENT CALENDAR FOR MARCH-MAY IS :")
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT * FROM ONE_ACTIVITY")
        while True:
            hd=cur1.fetchone()
            if hd==None:
                break
            print(hd[0],".    Event name:",hd[1],"          ON:",hd[4])
        obj1.close()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("DELETE FROM FOUR_ACTIVITY WHERE SNO>%s"%(0,))
        obj1.commit()
        obj1.close()
    else:
        print()
        print("                          *********** WRONG INPUT ***********")
        print()
def recruit():
    print(" **************************************************************************************************")
    while True:
        date=input("Enter Today's Date (YYYY-MM-DD) :")
        print()
        print("1. Engineer")
        print("2. Manager")
        print("3. Sr.manager ")
        print("4. Chief manager ")
        print("5. DGM")
        print()
        t=input("Enter the desigantion for which you want to recruit people (1-5) :")
        print()
        if t=='1':
            oi='ENGINEER'
            sal=20000
            qual='B.TECH'
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM APPLICANTS WHERE DEGREE='%s'"%(qual))
        elif t=='2':
            oi='MANAGER'
            sal=30000
            qual='B.TECH + MA(computers)'
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM APPLICANTS WHERE DEGREE='%s'"%(qual))
        elif t=='3':
            oi='SR.MANAGER'
            sal=35000
            qual='B.TECH + M.TECH'
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM APPLICANTS WHERE DEGREE='%s' AND EXPIR_YEARS=%s"%(qual,2))
        elif t=='4':
            oi='CHIEF MANAGER'
            sal=40000
            qual='B.TECH + M.TECH'
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM APPLICANTS WHERE DEGREE='%s' AND EXPIR_YEARS=%s"%(qual,3))
        elif t=='5':
            oi='DGM'
            sal=50000
            qual='B.TECH + M.TECH'
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM APPLICANTS WHERE DEGREE='%s' AND EXPIR_YEARS=%s"%(qual,4))
        else:
            print()
            print("    ********************** WRONG INPUT ***********************")
            print()
            print(" ********************* PLEASE TRY AGAIN **********************")
            print()
            continue
        i=1
        items=[]
        jojo=[]
        while True:
            s=cur1.fetchone()
            items.append(s)
            if s==None:
                break
            print()
            print("APPLICANT",i)
            print("    Applicant_id :",s[0])
            jojo.append(s[0])
            print("    Name :",s[1])
            print("    Age :",s[2])
            print("    Degree :",s[3])
            print("    Institution :",s[4])
            print("    Expirience :",s[5],"years")
            print("    Innovations :",s[6],"on AI")
            i+=1
        obj1.close()
        print()
        j=input("Enter the applicant_id of the employee you want to recruit into Candela :")
        while j.isdigit()==False:
            j=input("   Please Enter a digit :")
        while int(j) not in jojo:
            j=input("   Please enter only those applicant id that are dislayed above :")
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT * FROM APPLICANTS WHERE SNO=%s"%(j))
        g=cur1.fetchone()
        obj1.close()
        print()
        print("DO YOU WISH FOR THE FOLLOWING APPLICANT TO HOLD THE OFFICE OF",oi)
        print()
        print("    Name :",g[1])
        print("    Age :",g[2])
        print("    Degree :",g[3])
        print("    Institution :",g[4])
        print("    Expirience :",g[5],"years")
        print("    Innovations :",g[6],"on AI")
        print()
        ch=input("ENTER FINAL CHOICE (yes/no) :")
        print()
        if ch in ('yes','YES','Yes'):
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("DELETE FROM APPLICANTS WHERE SNO=%s"%(j))
            obj1.commit()
            obj1.close()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM EMPLOYEE")
            data=cur1.fetchall()
            obj1.close()
            print()
            print("***** BOOKQUE AND CONGO LETTER SUCCESSFULLY SENT TO MR.",g[1],"*****")
            import random
            reply=random.randint(1,2)
            if reply==1:
                print()
                print(" Mr.",g[1],"has accepted the offer of the company and will be joing from today!!! (^__^)")
                y=data[-1][0]
                y=y[-1:-3]
                sno='CAN0'+y
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute("INSERT INTO EMPLOYEE VALUES('{}','{}','{}','{}',{},'{}')".format(sno,g[1],'DESIGN',oi,sal,date))
                obj1.commit()
                cur1.close()
                print()
                print(" MR.",g[1],"has been successfully entred into the employee list..........")
            else:
                print()
                reason=random.randint(1,4)
                if reason==1:
                    reason="Has been recruited into another company with prior commitment"
                elif reason==2:
                    reason="Has a pending case of crime in court"
                elif reason==3:
                    reason="On investigation, he is no person in real but a fake identity"
                else:
                    reason="Is dead"
                print('Mr.',g[1],"will not be able to join the job as",reason)
                print()
                break
        elif ch in ('NO','No','no'):
            print()
            print("                ***************** OK, NO PROBLEM ****************")
            print()
            print("     *************** AUTO DIRECTION TO MAIN MENU ******************")
            print()
            break
        else:
            print()
            print("    ********************** WRONG INPUT ***********************")
            print()
            print(" ********************* PLEASE TRY AGAIN **********************")
            print()
            continue
        choice=input("Do you want to recruit more people in Candela (yes/no)? :")
        if choice in ("YES",'yes','Yes'):
            continue
        elif choice in ("NO",'no',"No"):
            break
        else:
            print()
            print("    ********************** WRONG INPUT ***********************")
            print()
            print("    ************* AUTO DIRECTION TO MAIN MENU *************")
            print()
            break
def complaint():
    while True:
        print()
        print("*****************************************************************************************************")
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute("SELECT EMP_ID FROM EMPLOYEE")
        datas=cur1.fetchall()
        obj1.close()
        items=[]
        for i in datas:
            items.append(i[0])
        name=input("Enter the id of the employee against whom complaint has to be registered (for eg, CAN001) :")
        if name not in items:
            print()
            print("No employee with emp_id",name,"works in candela.")
            print()
            print("             ************* COMPLAINT REQUEST DENIED *************")
            print()
            print(" ************************* PLEASE TRY AGAIN *****************************")
            break
        print()
        print("1. Women teasing/harrassment")
        print("2. Financial theft")
        print("3. Involvement in a fight")
        print("4. Continous fever")
        print("5. Revealing secreats of the company")
        print("6. Unauthorized videography in the factory")
        print("7. Leisuring while worktime")
        print("8. Continous late at work")
        print("9. Continously unable to finish assigned goals.")
        print()
        h=input("Enter the activity through which the emloyee has broken the code of conduct (1-9) :")
        if h in ('1','2','5'):
            print()
            print("Candela's offices consider this crimes among the highest offences and employee",name,"has been directly kicked out from the job.")
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("DELETE FROM EMPLOYEE WHERE EMP_ID='%s'"%(name))
            obj1.commit()
            obj1.close()
            print()
            print("EMPLOYEE HAS BEEN SUCCESFULLY DELETED FROM EMPLOYEE DATABASE...")
            print()
        elif h in ('3','6'):
            print()
            print("This crimes are taken seriously by Candela and the employee has been deducted with 15 points and a warning !!!")
            print()
            print("The employee will be automatically kicked out from Candela on the third warning !!!")
            print()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT *  FROM EMPLOYEE WHERE EMP_ID='%s'"%(name))
            ffff=cur1.fetchone()
            print(ffff)
            obj1.close()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            abcd=ffff[6]-15
            efgh=ffff[7]+1
            cur1.execute("UPDATE EMPLOYEE SET POINTS={} AND NO_WARNING={} WHERE EMP_ID='{}'".format(abcd,efgh,name))
            obj1.commit()
            obj1.close()
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("SELECT * FROM EMPLOYEE WHERE NO_WARNING=%s"%(3))
            erase=cur1.fetchone()
            obj1.close()
            if erase!=None:
                print()
                print("The number of warnings of employee",erase[0],"i.e",erase[1],"became three and thus,he has been removed from Candela !!!") 
                print()
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute("DELETE FROM EMPLOYEE WHERE EMP_ID='%s'"%(name))
                obj1.close()
                print("EMPLOYEE HAS BEEN SUCCESFULLY DELETED FROM EMPLOYEE DATABASE...")
                obj1.commit()
                print()
                obj1.close()   
        elif h in ('4','7','8','9'):
            print()
            print("Candela considers this as a soft crime (not much to be punished about) and the offender has been deducted with 10 points")
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            cur1.execute("UPDATE EMPLOYEE SET POINTS=POINTS-%s WHERE EMP_ID='%s'"%(10,name))
            obj1.commit()
            obj1.close()
        else:
            print()
            print(" ********* PLEASE CHOOSE FROM THE ABOVE MENTIONED ACTS *********")
            print()
            continue
        choice=input('Do you want to register more complaints against Candela employees (yes/no) :')
        if choice in ("YES",'yes','Yes'):
            continue
        elif choice in ("NO",'no',"No"):
            break
        else:
            print()
            print("    ********************** WRONG INPUT ***********************")
            print()
            print("    ************* AUTO DIRECTION TO MAIN MENU *************")
            print()
            break
def bonus():
    print()
    print("***************************************************************************************************************")
    print()
    while True:
        total_budget=int(input("Enter the total budget of bonus distribution (For eg, 2000000):"))
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT POINTS FROM EMPLOYEE')
        p=[]
        while True:
            dodo=cur1.fetchone()
            if dodo==None:
                break
            p.append(dodo)
        su=0
        obj1.close()
        for i in p:
            su+=i[0]
        avg=su/len(p)
        print("The average points in the company is :",avg)
        print()
        cri=int(input("Decide the minimum number of points after which bonus will offered (For eg,14) :"))
        print()
        each=int(input("What will be the bonus given on each point after the critical point (For eg,2000) :"))
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT * FROM EMPLOYEE')
        count=0
        total_amount=0
        while True:
            r=cur1.fetchone()
            if r==None:
                break
            if r[6]>=cri:
                dif=r[6]-cri
                bon=(dif+1)*each
                total_amount+=bon
                count+=1
        obj1.close()
        if total_amount>total_budget:
            print()
            print("THE TOTAL BONUS AMOUNT HAS BECOME MORE THAN THE BUDGET FOR BONUS...")
            print()
            print("1. Again calculate bonus amount with less money on each point and higher minimum value")
            print("2. Issue loan amount from investors (12 % interest per month)")
            print("3. Cancel the bonus this quater ;__;")
            print()
            ch=input("What do you want to do now (1-3)? :")
            if ch=='1':
                continue
            elif ch=='2':
                import random
                you=random.randint(1,5)
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute('SELECT NAME FROM INVESTORS')
                yout=cur1.fetchall()
                obj1.close()
                investor=yout[you-1][0]
                difference=total_amount-total_budget
                print("Searching for investors.....")
                print('.')
                print('.')
                print('.')
                print('.')
                print("Loan amount of",difference,"$ has been financed from",investor,"debt at 12% interest per month.")
                total_amount=total_budget
            elif ch=='3':
                print()
                print("OK, BONUS HAS BEEN CANCELLED THIS QUATER.....")
                print()
                print("SORRY LETTER SENT TO THE EMPLOYEES FOR NO BONUS THIS QUATER  (;__;)")
                print()
                break
            else:
                print()
                print("                 ***************** WRONG INPUT *****************")
                print()
                print("       ************** AUTO DIRECTION TO MAIN MENU ***************")
                print()
                break
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT EMP_ID,POINTS FROM EMPLOYEE WHERE POINTS>=%s'%(cri))
        g=[]
        points=[]
        while True:
            d=cur1.fetchone()
            if d==None:
                break
            g.append(d[0])
            points.append(d[1])
        obj1.close()
        for i in range(len(g)):
            obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
            cur1=obj1.cursor()
            X=each*((points[i]+1)-cri)
            cur1.execute("UPDATE EMPLOYEE SET POINTS=%s AND BONUS=%s WHERE EMP_ID='%s'"%(0,X,g[i]))
            obj1.commit()
        print()
        print("SUCCESSFULLY GIVEN ALL THE DESERVING PEOPLE BONUS FOR THE QUATER.....(^___^)")
        print()
        break
while True:
    print()
    print("1. TO DESIGN THE ACTIVITY CALENDAR FOR THE NEXT QUATER")
    print("2. TO MANAGE RECRUITMENT AND SELECTION")
    print("3. TO REGISTER COMPLAINTS AGAINST ANY EMPLOYEE")
    print("4. TO CALCULATE BONUS OF EMPLOYEES ACCRODING TO POINTS")
    print("5. EXIT")
    print()
    w=input("Enter Your Choice (1-5) :")
    if w=='1':
        calendar()
    elif w=='2':
        recruit()
    elif w=='3':
        complaint()
    elif w=='4':
        bonus()
    elif w=='5':
        print()
        print("                          *************** THANK YOU FOR USING THE HR INTERFACE *************")
        print()
        break
    else:
        print()
        print("                                                  ***************** WRONG INPUT ***************")
        print()
        print("                                     ************** AUTO DIRECTION TO MAIN MENU ****************")
        print()
