import mysql.connector as mycon
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print("                          ************************ WELCOME TO THE FINANCE INTERFACE **********************")
print()
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
def budget():
    print("***************************************************************************************************************")
    print()
    while True:
        a=int(input("How many cars does the company aim to sell the net quater(For eg 50000000000) :"))
        print()
        print("Budget preparation for Candela involves the following steps:")
        print("      1. Collecting information from all departments")
        print("      2. Evaluation and developing the budget report")
        print("      3. Distribution of the budget in various departments")
        print()
        print("INITIALIZING STEP1 :COLLECTING INFORMATION FROM VARIOUS DEPARTMENTS")
        print()
        print("1. MANUFACTURING DEPARTMENT")
        s1=int(input("Enter the total expense to be done in R&D (For eg,100000) :"))
        s2=int(input("How much money does the factory requires for maintainance in a day (For eg, 5000) :"))
        print("Thus, amount to be spend on the factory in the whole quater is",s2*120)
        s2=s2*120
        print("Enter overhead charges:")
        s3=int(input("    Enter the cost of electricity per Kwh (For eg, 10) :"))
        s4=int(input("    Enter the electricity consumed per day in Kwh (For eg, 200) :"))
        s3=s3*s4*120
        s5=int(input("    Enter the cost of water per gallon (For eg, 65) :"))
        s6=int(input("    Enter the water consumed per day in gallons (For eg,8000000000) :"))
        s5=s5*s6*120
        print("The Manufacturing department has asked for a budget amount of",s1+s2+s3+s5,"for the next quater.")
        bug_manu=s1+s2+s3+s5
        print()
        print("2. PURCHASE AND STORE DEPARTMENT")
        t1=int(input("Enter the total expense to be done in space enlargement (For eg,100000 :"))
        t2=int(input("How much money requires for dameged items'compensation (For eg, 50000) :"))
        print("Since the number of cars aimed by the company for the next quater is",a)
        t3=int(input("Enter the cost of raw materials for a single car (For eg,5000) :"))
        t3=t3*a
        t4=int(input("Enter the total amount to be spent on insurance of goods :"))
        print("The Store and Purchase department has asked for a budget amount of",t1+t2+t3+t4,"for the next quater.")
        bug_pur=t1+t2+t3+t4
        print()
        print("3. HR DEPARTMENT")
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT SALARY FROM EMPLOYEE')
        L=0
        while True:
            g=cur1.fetchone()
            if g==None:
                break
            L+=g[0]
        obj1.close()
        print("The salary cost for all employees in a month is ",L,'$',sep='')
        L=L*4
        p=0.3*L
        print("The PF cost for all employees in a month is",p,"30% of the salary of each employee")
        print("The HR department has asked for a budget amount of",L+p,"for the next quater.")
        bug_hr=L+p
        print()
        print("4. MARKETING DEPARTMENT")
        m1=int(input("Enter the total cost to be spent on advertising :"))
        m2=int(input("Enter the budget of investment of candela into other startups :"))
        m3=int(input("Enter the total cost on free product giveaways and cometitions :"))
        m4=int(input('Enter the budget of sponsoring events/companies/etc :'))
        print("The Marketing department has asked for a budget amount of",m1+m2+m3+m4,"for the next quater.")
        bug_mar=m1+m2+m3+m4
        print()
        print()
        print("INITIALIZING STEP 2 : EVALUATION OF BUDGET REPORT ")
        print()
        print("The total budget of the factory makes upto :",bug_manu+bug_mar+bug_pur+bug_hr)
        print("    Manufacturing :",bug_manu)
        print("    Purchase and Store :",bug_pur)
        print("    HR :",bug_hr)
        print("    Marketing :",bug_mar)
        print()
        mar=int(input("Enter the profit aimed margin of the company over the next quater (in %) (For eg: 20) :"))
        print(mar,"% of",bug_manu+bug_mar+bug_pur+bug_hr,"is",(mar/100)*(bug_manu+bug_mar+bug_pur+bug_hr))
        print()
        obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
        cur1=obj1.cursor()
        cur1.execute('SELECT BASE_PRICE FROM CATALOG')
        dd=0
        count=0
        while True:
            df=cur1.fetchone()
            if df==None:
                break
            dd+=int(df[0])
            count+=1
        obj1.close()
        avg=dd/count
        total_budget=(bug_manu+bug_mar+bug_pur+bug_hr)+((mar/100)*(bug_manu+bug_mar+bug_pur+bug_hr))
        if total_budget>(a*avg):
            print("The buget does not meets the profit demands of the company since total cost is becoming more than forecasted sales !!!")
            print()
            print("1. To recalculate the budgets")
            print("2. To decrease the profit target")
            print("3. To increase the cost of cars")
            print()
            u=input("Enter your choice (1-3) :")
            print(total_budget)
            print(a*avg)
            if u=='1':
                continue
            elif u=='2':
                mar=int(input("Enter the profit aimed margin of the company over the next quater (For eg: 20%) :"))
                total_budget=(bug_manu+bug_mar+bug_pur+bug_hr)+((mar/100)*(bug_manu+bug_mar+bug_pur+bug_hr))
                while total_budget>(a*avg):
                    print("    The margin was again high,seek a lower one")
                    mar=input("    Enter the profit aimed margin of the company over the next quater (For eg: 20%) :")
            elif u=='3':
                differ=(total_budget-(a*avg))
                print("Rising the price of each car by",differ/10,"$")
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute("UPDATE CATALOG SET BASE_PRICE=BASE_PRICE-%s"%(differ))
                obj1.close()
                print()
                print("Successfully increased the base_price by",differ)
            else:
                print()
                print("                                    ******************** WRONG INPUT *******************")
                print()
                print("                         *********************** PLEASE TRY AGAIN **************************")
                print()
                break
        print()
        print()
        print("STEP 3 : DISTRIBUTION WITHIN THE DEPARTMENTS")
        print()
        print("    Manufacturing :",bug_manu)
        print("    Purchase and Store :",bug_pur)
        print("    HR :",bug_hr)
        print("    Marketing :",bug_mar)
        print()
        tuples=(bug_mar,bug_manu,bug_hr,bug_pur)
        choice_=input("Do you want to transfer this budget within the departments (yes/no)? :")
        if choice_=='yes':
            i=0
            while True:
                if i==4:
                    break
                obj1=mycon.connect(host='localhost',user='root',password='root123',database='CANDELA')
                cur1=obj1.cursor()
                cur1.execute('UPDATE DEPARTMENTS SET BUDGET=%s'%(tuples[i]))
                obj1.close()
                i+=1
            print()
            print("              *************** SUCCESSFULLY UPDATED THE BUDGET COLUMNS **************")
            break
        elif choice_=='no':
            break
        else:
            break
def sales():
    print()
    print("***************************************************************************************************")
    print()
    time=int(input("From which year do you want to consider the trend (For eg, 2009) :"))
    h=2022-time
    i=0
    sales=[]
    years=[]
    while True:
        i+=1
        if i>h:
            break
        print("IN",time)
        o=input("    Enter the sales of the year :")
        while o.isdigit()==False:
            o=input("        Please enter a legible sales value (For eg, 200000000) :")
        sales.append(int(o))
        years.append(time)
        time+=1
    sume=0
    for i in range(len(sales)):
        sume=sume+int(sales[i])
    avg=sume/len(sales)
    print()
    print("THE predicted sales for the net year would be :",avg)
    years.append(2022)
    sales.append(avg)
    import numpy as n
    import matplotlib.pyplot as pl
    pl.plot(years,sales)
    pl.xlabel('years --------------------------->')
    pl.ylabel('sales ---------------------------->')
    pl.show()
    return avg
while True:
    print()
    print("1. TO PREPARE THE BUDGET FOR THE NEXT QUATER.")
    print("2. TO FORECAST THE SALES OF THE COMPANY")
    print("3. EXIT")
    print()
    choice=input("Enter your choice (1-3) :")
    if choice=='1':
        budget()
    elif choice=='2':
        sales()
    elif choice=='3':
        print()
        print("       ***********************  THANK YOU FOR USING THE FINANCE INTERFACE ************************")
        print()
        break
    else:
        print()
        print("                                         *********************** WRONG INPUT **********************")
        print()
        print("                                   ************************ PLEASE TRY AGAIN ************************")
