import csv
def adch():                                                      #coding to add social media influencers and the information of deals with them and to make changes in the database 
       while True :
              print("What do you want to proceed with ?")
              print(" 1. Add more records into our database. ")
              print(" 2. Make changes in the database ")
              print(" 3. Move back to previous menu")
              input("Press Enter")
              ch=int(input("Enter your choice number from the above options :"))
              input("Press Enter")
              if ch==1:
                     fh=open("socmed.csv","a",newline='')
                     wri=csv.writer(fh)
                     print(" Before you proceed we would like to tell you the terms and conditions on the basis of which our company selects the youtubers !")
                     input("Press Enter to view the terms and conditions. Press enter after every condition to view the next condition")
                     print(" 1. The number of followers of the influencer should not be less than 1000000.")
                     input()
                     print('''This was the conditions of our company which the Influencer should be eligible of, for convinience.
                               Press enter in the next step to continue''')
                     print()
                     print()
                     print()
                     input("Press Enter to continue")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     num=int(input("Enter the number of influencers you want to enter (influencer might be not selected if the terms and conditions are not fulfilled:"))
                     for i in range(num):
                            nam=input("Enter the name of the Influencer :")
                            socp=int(input("Enter the social media platform of the influencer"))
                            fo=int(input("Enter the  number of followers of the influencer:" ))
                            dos=input("Enter the date from which the contract is expected to start MM/DD/YYYY :")
                            doe=input("Enter the date on which the contract is expected to end MM/DD/YYYY:")
                            if fo<1000000:
                                   print(" Sorry :( the influencer is not eligible for helping us in advertisement.")
                                   continue
                            else:
                                   amt1=0
                                   if 1000000<=fo<3000000:
                                          amt1=50
                                   elif 3000000<=fo<5000000:
                                          amt1=100
                                   elif 5000000<=fo<10000000:
                                          amt1=150
                                   elif 10000000<=sub<15000000:
                                          amt1=200
                                   elif 30000000<=sub<50000000:
                                          amt1=250
                                   elif 50000000<=sub<70000000:
                                          amt1=300
                                   elif 70000000<=sub:
                                          amt1=350
                            print(" Amount on the basis of number of followers is :",amt1)
                            print()
                            print()
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            amount='$'+str(amt1)
                            print('The final amount to be payed to the Influencer is:',amount)
                            lst=[nam,str(socp),str(fo),dos,doe,amount]
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
                     fh=open("socmed.csv","r",newline='')
                     re=csv.reader(fh)
                     y=list(re)
                     fh.close()
                     print(" Choose what changes do you want  to make ")
                     print(" 1. To make any changes in the deal of  influencer ") 
                     print(""" 2. To remove a particular influencer's record from the database
                     (By selecting this option you will be able to delete the record of any one influencer at a given chance) """)
                     print(" 3. Move back to previous menu")
                     Ch=int(input("Enter your choice number from the above options :"))
                     if Ch==1:
                            t=int(input(" Enter the number of influencers whose information you wanna change :"))
                            m=len(y)
                            for i in range(t):
                                   nam=input(" Enter the name of the influencer whose information you wanna change :")
                                   for j in range(m):
                                          if y[j][0]==nam:
                                                 k=int(input("Enter the number of times you want to edit the records of this influencer:"))
                                                 for s in range(k):
                                                        fh=open("socmed.csv","w",newline='')
                                                        wri=csv.writer(fh)
                                                        print("what do you want to change ?")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print(" 1. Change the name of the influencer.")
                                                        print(" 2. Change the type of social media platform used by the Influencer")
                                                        print(" 3. Change the number of followers of the influencer.")
                                                        print(" 4. Change the date of start of contract.")
                                                        print(" 5. Change the date of end of contract.")
                                                        print(" 6. Change the amount to be payed to the influencer.")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                                        input("Press Enter")
                                                        cH=int(input("Enter your choice number from the above options :"))
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        if cH==1:
                                                               name=input(" enter the new name of the influencer :")
                                                               y[j][0]=name
                                                        elif cH==2:
                                                               num=input(" enter the new the type of social media platform used by the influencer :")
                                                               y[j][1]=num
                                                        elif cH==3:
                                                               fol=input(" enter the new number of followers of the influencer.")
                                                        elif cH==4:
                                                               dos=input(" enter the new date of start of contract of the youtuber :")
                                                               y[j][3]=dos
                                                        elif cH==5:
                                                               doe=input(" enter the new date of end of contract of the influencer :")
                                                               y[j][4]=doe
                                                        elif cH==6:
                                                               amt=input(" enter the new amt to be payed to the influencer per post :")
                                                               y[j][5]=avg
                                                        wri.writerows(y)
                                                        print(" Successfully made the changes :)")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                          else:
                                                 continue
                                   else:
                                          print(" Sorry influencer with the entered name not found :(")
                                          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                          print()
                                          print()
                                          print()
                                          continue
                     elif Ch==2:
                            name=input(" Enter the name of the influencer related to whom you want to delete the record :")
                            m=len(y)
                            for i in range(0,m):
                                   if y[i][0]==name:
                                          fh=open("socmed.csv","w",newline='')
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
                                   print(" Sorry influencer with the entered name not found :(")
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
