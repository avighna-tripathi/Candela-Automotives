import csv
def adch():                                                      #coding to add television & radio channel and the information of deals with them and to make changes in the database 
       while True :
              print("What do you want to proceed with ?")
              print(" 1. Add more records into our database. ")
              print(" 2. Make changes in the database ")
              print(" 3. Move back to previous menu")
              input("Press Enter")
              ch=int(input("Enter your choice number from the above options :"))
              input("Press Enter")
              if ch==1:
                     fh=open("tvrad.csv","a",newline='')
                     wri=csv.writer(fh)
                     print(" Before you proceed we would like to tell you the terms and conditions on the basis of which our company selects the channels !")
                     input("Press Enter to view the terms and conditions. Press enter after every condition to view the next condition")
                     print(" 1. The length of advertsiement should not be less than 15 seconds.")
                     input()
                     print(" 2. The proposed number of times the advertisement to be broadcasted should not be less than 7")
                     input()
                     print('''These were the terms and conditions of our company which the Channel should be eligible of, for convinience.
                               Press enter in the next step to continue''')
                     print()
                     print()
                     print()
                     input("Press Enter to continue")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     num=int(input("Enter the number of channels you want to enter (channel might not be selected if the terms and conditions are not fulfilled):"))
                     for i in range(num):
                            nam=input("Enter the name of the channel :")
                            tr=input("Enter the type of broadcaster ( type only Television/Radio or television/radio and also in the same fashion for covienience) :")
                            dos=input("Enter the date from which the contract is expected to start MM/DD/YYYY :")
                            doe=input("Enter the date on which the contract is expected to end MM/DD/YYYY:")
                            length=int(input(" Enter the length of advertisement (in seconds) :"))
                            ti=int(input(" Enter the no of times the advertisement is broadcasted in a day :"))
                            if length<15 or ti<7:
                                   print(" Sorry :( the channel is not eligible for helping us in advertisement.")
                                   continue
                            else:
                                   amt1=0
                                   amt2=0
                                   amt3=0
                                   if 7<=length<10:
                                          amt1=10
                                   elif 10<=length<20:
                                          amt1=15
                                   elif 20<=length<30:
                                          amt1=25
                                   elif 30<=length:
                                          amt1=35      
                            print(" Amount on the basis of the length of advertisement (in seconds) is :",amt1)
                            print()
                            print()
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            if tr=='Television' or tr=='television':
                                   amt2=90
                            elif tr=='Radio' or tr=='radio':
                                   amt2=50
                            else:
                                   print(" Wrong value entered in type of marketing")
                                   continue
                            print(" Amount on the basis of type of channel is :",amt2)
                            print()
                            print()
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            amt3=amt2+amt1
                            amt=amt3*(ti/20)
                            amount='$'+str(amt)
                            print('The final amount to be payed to the channel per month is:',amount)
                            lst=[nam,tr,dos,doe,str(length),str(ti),amount]
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
                     fh=open("tvrad.csv","r",newline='')
                     re=csv.reader(fh)
                     y=list(re)
                     fh.close()
                     print(" Choose what changes do you want  to make ")
                     print(" 1. To make any changes in the deal of  channel ") 
                     print(""" 2. To remove a particular channel's record from the database
                     (By selecting this option you will be able to delete the record of any one youtuber at a given chance) """)
                     print(" 3. Move back to previous menu")
                     Ch=int(input("Enter your choice number from the above options :"))
                     if Ch==1:
                            t=int(input(" Enter the number of channels whose information you wanna change :"))
                            m=len(y)
                            for i in range(t):
                                   nam=input(" Enter the name of the channel whose information you wanna change :")
                                   for j in range(m):
                                          if y[j][0]==nam:
                                                 k=int(input("Enter the number of times you want to edit the records of this channel:"))
                                                 for s in range(k):
                                                        fh=open("tvrad.csv","w",newline='')
                                                        wri=csv.writer(fh)
                                                        print("what do you want to change ?")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print(" 1. Change the name of the channel.")
                                                        print(" 2. Change the type of broadcaster.")
                                                        print(" 3. Change the date of start of contract.")
                                                        print(" 4. Change the date of end of contract.")
                                                        print(" 5. Change the length of advertisement(in seconds)")
                                                        print(" 6. Change the number of times the advertisement is broadcasted per day")
                                                        print(" 7. Change the amount to be payed to the channel per month.")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                                        input("Press Enter")
                                                        cH=int(input("Enter your choice number from the above options :"))
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        if cH==1:
                                                               name=input(" enter the new name of the channel :")
                                                               y[j][0]=name
                                                        elif cH==2:
                                                               ty=input(" enter the new the type of broadcaster :")
                                                               y[j][1]=ty
                                                        elif cH==3:
                                                               dos=input(" enter the new date of start of contract of the channel :")
                                                               y[j][2]=dos
                                                        elif cH==4:
                                                               doe=input(" enter the new date of end of contract of the channel :")
                                                               y[j][3]=doe
                                                        elif cH==5:
                                                               length=input(" enter the new the length of advertisement(in seconds) :")
                                                               y[j][4]=length
                                                        elif cH==6:
                                                               ti=input(" enter the number of times the advertisement is broadcasted per day :")
                                                               y[j][5]=ti
                                                        elif cH==7:
                                                               amt=input(" enter the new amount to be payed to the channel per month :")
                                                               y[j][6]='$'+amt
                                                        wri.writerows(y)
                                                        print(" Successfully made the changes :)")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                          else:
                                                 continue
                                   else:
                                          print(" Sorry channel with the entered name not found :(")
                                          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                          print()
                                          print()
                                          print()
                                          continue
                     elif Ch==2:
                            name=input(" Enter the name of the channel related to whom you want to delete the record :")
                            m=len(y)
                            for i in range(0,m):
                                   if y[i][0]==name:
                                          fh=open("tvrad.csv","w",newline='')
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
                                   print(" Sorry the channel with the entered name not found :(")
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
