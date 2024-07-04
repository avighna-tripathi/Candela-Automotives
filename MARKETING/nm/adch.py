import csv
def adch():                                                      #coding to add Newspaper & Magazine and the information of deals with them and to make changes in the database 
       while True :
              print("What do you want to proceed with ?")
              print(" 1. Add more records into our database. ")
              print(" 2. Make changes in the database ")
              print(" 3. Move back to previous menu")
              input("Press Enter")
              ch=int(input("Enter your choice number from the above options :"))
              input("Press Enter")
              if ch==1:
                     fh=open("newsmag.csv","a",newline='')
                     wri=csv.writer(fh)
                     print(" Before you proceed we would like to tell you the terms and conditions on the basis of which our company selects the Newspapers & Magazines !")
                     input("Press Enter to view the terms and conditions. Press enter after every condition to view the next condition")
                     print(""" 1. The No of times ad is printed in an edition per month should not be less than 6 for Magazines and 10 for Newspapers.""")
                     input()
                     print(""" 2. The No of Front/Cover Page appearances in newspaper/magazine per month should not be less than 2 for magazine and 6 for newspapers""")
                     print('''These were the terms and conditions of our company which the daily should be eligible of, for convinience.
                               Press enter in the next step to continue''')
                     print()
                     print()
                     print()
                     input("Press Enter to continue")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     num=int(input("Enter the number of dailies you want to enter (daily might be not selected if the terms and conditions are not fulfilled):"))
                     for i in range(num):
                            nam=input("Enter the name of the channel :")
                            mn=input("Enter the type of daily ( type only Newspaper/magazines or newspaper/magazine and also in the same fashion for covienience) :")
                            dos=input("Enter the date from which the contract is expected to start MM/DD/YYYY :")
                            doe=input("Enter the date on which the contract is expected to end MM/DD/YYYY:")
                            pm=int(input(" Enter the No of times ad is printed in an edition per month :"))
                            fc=int(input(" Enter the no of times the advertisement is printed on the front/cover page in a newspaper/magazine per month:"))
                            if (mn=='newspaper' and pm<10) or (mn=='Newspaper' and pm<10) or (mn=='NEWSPAPER' and pm<10):
                                   print(" Sorry :( the daily is not eligible for helping us in advertisement.")
                                   continue
                            elif (mn=='magazine' and pm<6) or (mn=='Magazine' and pm<6) or (mn=='MAGAZINE' and pm<6) :
                                   print(" Sorry :( the daily is not eligible for helping us in advertisement.")
                                   continue
                            elif (mn=='newspaper' and fc<6) or (mn=='Newspaper' and fc<6) or (mn=='NEWSPAPER' and fc<6):
                                   print(" Sorry :( the daily is not eligible for helping us in advertisement.")
                                   continue
                            elif (mn=='magazine' and fc<2) or (mn=='Magazine' and fc<2) or (mn=='MAGAZINE' and fc<2) :
                                   print(" Sorry :( the daily is not eligible for helping us in advertisement.")
                                   continue
                            else:
                                   amtn=10
                                   amtm=5
                                   if mn=='newspaper' or mn=='Newspaper' or mn=='NEWSPAPER':
                                          amt=amtn*(pm/2)*(fc/2)
                                   elif mn=='magazine' or mn=='Magazine' or mn=='MAGAZINE':
                                          amt=amtm*(pm/2)*(fc/2)
                            amount='$'+str(amt)
                            print('The final amount to be payed to the channel per month is:',amount)
                            lst=[nam,mn,dos,doe,str(pm),str(fc),amount]
                            print(' We are going to enter the following record:  ',lst)
                            wri.writerow(lst)
                            print()
                            print()
                            print()
                            print(" Yay :) Successfully entered the record")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            input("Press Enter")
                            print()
                            print()
                            print()
                     fh.close()
              elif ch==2:
                     fh=open("newsmag.csv","r",newline='')
                     re=csv.reader(fh)
                     y=list(re)
                     fh.close()
                     print(" Choose what changes do you want  to make ")
                     print(" 1. To make any changes in the deal of  daily ") 
                     print(""" 2. To remove a particular daily's record from the database
                     (By selecting this option you will be able to delete the record of any one daily at a given chance) """)
                     print(" 3. Move back to previous menu")
                     Ch=int(input("Enter your choice number from the above options :"))
                     if Ch==1:
                            t=int(input(" Enter the number of dailies whose information you wanna change :"))
                            m=len(y)
                            for i in range(t):
                                   nam=input(" Enter the name of the daily whose information you wanna change :")
                                   for j in range(m):
                                          if y[j][0]==nam:
                                                 k=int(input("Enter the number of times you want to edit the records of this newsmag:"))
                                                 for s in range(k):
                                                        fh=open("newsmag.csv","w",newline='')
                                                        wri=csv.writer(fh)
                                                        print("what do you want to change ?")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print(" 1. Change the name of the daily.")
                                                        print(" 2. Change the type of daily ( type only Newspaper/magazines or newspaper/magazine and also in the same fashion for covienience).")
                                                        print(" 3. Change the date of start of contract.")
                                                        print(" 4. Change the date of end of contract.")
                                                        print(" 5. Change the No of times ad is printed in an edition per month")
                                                        print(" 6. Change the no of times the advertisement is printed on the front/cover page in a newspaper/magazine per month")
                                                        print(" 7. Change the amount to be payed to the channel per month.")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                                        input("Press Enter")
                                                        cH=int(input("Enter your choice number from the above options :"))
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        if cH==1:
                                                               name=input(" enter the new name of the daily :")
                                                               y[j][0]=name
                                                        elif cH==2:
                                                               ty=input(" enter the new the type of daily ( type only Newspaper/magazines or newspaper/magazine and also in the same fashion for covienience) :")
                                                               y[j][1]=ty
                                                        elif cH==3:
                                                               dos=input(" enter the new date of start of contract of the daily :")
                                                               y[j][2]=dos
                                                        elif cH==4:
                                                               doe=input(" enter the new date of end of contract of the daily :")
                                                               y[j][3]=doe
                                                        elif cH==5:
                                                               length=input(" enter the new No of times ad is printed in an edition per month :")
                                                               y[j][4]=length
                                                        elif cH==6:
                                                               ti=input(" enter the new no of times the advertisement is printed on the front/cover page in a newspaper/magazine per month :")
                                                               y[j][5]=ti
                                                        elif cH==7:
                                                               amt=input(" enter the new amount to be payed to the daily per month :")
                                                               y[j][6]='$'+amt
                                                        wri.writerows(y)
                                                        print(" Successfully made the changes :)")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                                        fh.close()
                                          else:
                                                 continue
                                   else:
                                          print(" Sorry daily with the entered name not found :(")
                                          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                          print()
                                          print()
                                          print()
                                          continue
                     elif Ch==2:
                            name=input(" Enter the name of the daily related to whom you want to delete the record :")
                            m=len(y)
                            for i in range(0,m):
                                   if y[i][0]==name:
                                          fh=open("newsmag.csv","w",newline='')
                                          wri=csv.writer(fh)
                                          del y[i]
                                          wri.writerows(y)
                                          print(" Successfully made the changes :)")
                                          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                          print()
                                          print()
                                          print()
                                          break
                                   else:
                                          continue
                            else:
                                   print(" Sorry the daily with the entered name not found :(")
                                   print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                   print()
                                   print()
                                   print()
                     elif Ch==3:
                            print(" Moving back to previous menu :)")
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print()
                            print()
                            print()
                            break
                     else:
                            print(" Wrong option number entered. Try Again!")
              elif ch==3:
                     print(" Moving back to previous menu :)")
                     input("Press Enter")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     print()
                     print()
                     print()
                     break
              else:
                     print(" Wrong option number entered. Try Again!")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     print()
                     print()
                     print()

adch()
