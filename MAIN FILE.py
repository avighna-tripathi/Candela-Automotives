import creation_tables
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print("********* WELCOME  TO  CANDELA  AUTOMOTIVES ******* ")
print()
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print("""Candela Inc. is an Indian electric vehicle and clean energy company based in Kanpur,UP,India. Established in 2022,
by Avighna Tripathi and Divyansh Mishra, it is accelerating the world's transition to sustainable energy with automatic electric cars.""")
print()
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()            
a=input("           >>> press Enter key to continue <<<           ")
print("====================================================")
import mysql.connector as mycon
def admin_interface():
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print()
    print("*************WELCOME TO THE ADMIN INTERFACE************")
    print()
    h=input("Since this section has restricted view to the employees of candela only,Please enter COMPANY_ID:")
    while True:
        if h=='':
            print("Please enter your COMPANY_ID:")
        else:
            break
    if h=='CANDELA@SUCCESS':
        print()
        print("Hello buddy!!! This is the ADMIN interface")
        print()
        while True:
            print("1. Connect to Finance department")
            print("2. Connect to HR department")
            print("3. Connect to Purchase department")
            print("4. Connect to Marketing department")
            print("5. Connect to Plan maintanance server")
            print("6. Exit")
            print()
            sh=input("Enter your choice (1-6) :")
            if sh=='1':
                import Finance_software
            elif sh=='2':
                import HR_software
            elif sh=='3':
                import purchase_software
            elif sh=='4':
                from MARKETING import Marketing
            elif sh=='5':
                from Plms import plma
            elif sh=='6':
                break
            else:
                print()
                print("   ****** WRONG INPUT ******")
                print()
                print("******* PLEASE TRY AGAIN *******")
                continue
while True:
    print(" 1.USE THE ADMIN INTERFACE **Requires admin's pin**")
    print(" 2.USE THE USER INTERFACE")
    print(" 3.EXIT")
    print()
    b=input("Enter your role(1-4) :")
    print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    if b=='1':
        admin_interface()
    elif b=='2':
        import user_software
    elif b=='3':
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print()
        print(" ****** Thank you for contacting Candela Automotives ******")
        print(" ******  Wish To see You later ^_^******")
        print( "******Have a good day  :)  ******")                                                          
        break
    else:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print()
        print("********* Wrong Input   o_o*********")
        print(" *************** PLEASE TRY AGAIN  ***************")
        continue
