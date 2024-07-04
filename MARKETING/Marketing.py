print("                                                           Welcome to the Marketing Department of Candela Automobiles :)")
print()
print()
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print()
print()
print()
print(''' In this Department we give access to the user/admin to view as well make entries in our database regarding the Marketing section which includes various
modes through which our company does the marketing of our products i.e., automobiles''')
print()
print()
print()
print(''' The following menu will display you the various operations in our Department and also let you view them too:''')
input("Press Enter to continue")
print()
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
while True:
       print(' 1. To view the various modes through which we do the marketing of our products')
       print(' 2. To view the statistics of each of our modes of marketing')
       print(' 3. (For admin or official Only!!!) To make changes or add another entity in any of our modes of marketing')
       print(' 4. Back to the previous menu')
       input("Press Enter to continue")
       print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
       choice1=int(input(' Enter Your Choice number from the above options:'))
       if choice1==1:
              print(" The various Modes Of Marketing used By Candela Automobiles are:")
              print("1. Marketing through Youtube")
              print("2. Marketing through Social Media")
              print("3. Marketing through newspapers, magazines, etc.")
              print("4. Marketing through Television and radio")
              print()
              print()
              print()
       elif choice1==2:
              print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              print(" You have selected to view the statistics of each of our modes of marketing")
              print()
              print()
              print()
              print(" From the following menu select the option which has the mode of marketing whose statistics you wanna view .")
              print()
              print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              print("1. Marketing through Youtube")
              print("2. Marketing through Social Media")
              print("3. Marketing through newspapers, magazines, etc.")
              print("4. Marketing through Television and radio")
              print("5. Back to previous menu")
              print()
              print()
              print()
              print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              choice2=int(input(' Enter the your choice number from the above options :'))
              if choice2==1:
                     from youtube import view
              elif choice2==2:
                     from socialmedia import view
              elif choice2==3:
                     from nm import view
              elif choice2==4:
                     from tvrad import view
              elif choice2==5:
                     print(" Moving back to previous menu ")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     break
              else:
                     print(" Wrong Choice!! Try Again!!")
       elif choice1==3:
              print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              print(" You have selected to make changes or add another entity in any of our modes of marketing")
              print()
              print()
              print()
              print(""" From the following menu select the option which has the mode of marketing in which you want to make changes or add another entity
              in any of our modes of marketing  .""")
              print()
              print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              print("1. Marketing through Youtube")
              print("2. Marketing through Social Media")
              print("3. Marketing through newspapers, magazines, etc.")
              print("4. Marketing through Television and radio")
              print("5. Back to previous menu")
              print()
              print()
              print()
              print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              choice3=int(input(' Enter the your choice number from the above options :'))
              if choice3==1:
                     from youtube import adch
              elif choice3==2:
                     from socialmedia import adch
              elif choice3==3:
                     from nm import adch
              elif choice3==4:
                     from tvrad import adch
              elif choice3==5:
                     print(" Moving back to previous menu ")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     break
              else:
                     print(" Wrong Choice!! Try Again!!")
       elif choice1==4:
              print(" Thank you for giving us the opportunity to serve you :) ")
              print()
              print()
              print()
              break
       else:
              print(" Wrong option Try again ")
