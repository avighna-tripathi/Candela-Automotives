import csv
def adch():                                                      #coding to add youtubers and the information of deals with them and to make changes in the database 
       while True :
              print("What do you want to proceed with ?")
              print(" 1. Add more records into our database. ")
              print(" 2. Make changes in the database ")
              print(" 3. Move back to previous menu")
              input("Press Enter")
              ch=int(input("Enter your choice number from the above options :"))
              input("Press Enter")
              if ch==1:
                     fh=open("Youtubers.csv","a",newline='')
                     wri=csv.writer(fh)
                     print(" Before you proceed we would like to tell you the terms and conditions on the basis of which our company selects the youtubers !")
                     input("Press Enter to view the terms and conditions. Press enter after every condition to view the next condition")
                     print(" 1. The number of subscribers of the youtuber's YouTube channel should not be less than 5000.")
                     input()
                     print(" 2. The average number of views on each uploaded video of the youtuber should not be less than 5000")
                     input()
                     print('''These were the terms and conditions of our company which the Youtuber should be eligible of, for convinience.
                               Press enter in the next step to continue''')
                     print()
                     print()
                     print()
                     input("Press Enter to continue")
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     num=int(input("Enter the number of youtubers you want to enter (youtuber might be not selected if the terms and conditions are not fulfilled):"))
                     for i in range(num):
                            nam=input("Enter the name of the YouTuber :")
                            sub=int(input("Enter the number of subscribers(in international numbering system) of the YouTuber"))
                            dos=input("Enter the date from which the contract is expected to start MM/DD/YYYY :")
                            doe=input("Enter the date on which the contract is expected to end MM/DD/YYYY:")
                            vi=int(input("Enter the average number of views per video:" ))
                            mark=input("Enter the type of marketing (skipable/unskipable/in video) preferred by the youtuber :")
                            if sub<5000:
                                   print(" Sorry :( the youtuber is not eligible for helping us in advertisement.")
                                   continue
                            else:
                                   amt1=0
                                   amt2=0
                                   amt3=0
                                   if 5000<=sub<100000:
                                          amt1=5
                                   elif 100000<=sub<500000:
                                          amt1=10
                                   elif 500000<=sub<1000000:
                                          amt1=15
                                   elif 1000000<=sub<5000000:
                                          amt1=20
                                   elif 5000000<=sub<10000000:
                                          amt1=25
                                   elif 10000000<=sub<15000000:
                                          amt1=30
                                   elif 15000000<=sub:
                                          amt1=35
                            print(" Amount on the basis of number of subscribers is :",amt1)
                            print()
                            print()
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            if mark=='skipable' or mark=='Skipable' or mark=='SKIPABLE':
                                   amt2=10
                            elif mark=='unskipable' or mark=='Unskipable' or mark=='UNSKIPABLE':
                                   amt2=20
                            elif mark=='in video' or mark=='In video' or mark=='In Video' or mark=='IN VIDEO':
                                   amt2=25
                            else:
                                   print(" Wrong value entered in type of marketing")
                                   continue
                            print(" Amount on the basis of type of adverstisement chosen by the youtuber is :",amt2)
                            print()
                            print()
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            if 5000<=vi<500000:
                                   amt3=5
                            elif 500000<=vi<1000000:
                                   amt3=10
                            elif 100000<=vi<5000000:
                                   amt3=25
                            elif 5000000<=vi<10000000:
                                   amt3=30
                            elif 10000000<=vi:
                                   amt3=40
                            else:
                                   print("Sorry :( the youtuber is not eligible for helping us in advertisement.")
                                   continue
                            print(" Amount on the basis of the average number of view on each video of the YouTuber is:",amt3)
                            print()
                            print()
                            input("Press Enter")
                            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            amt=amt1+amt2+amt3
                            amount='$'+str(amt)
                            print('The final amount to be payed to the YouTuber is:',amount)
                            lst=[nam,str(sub),dos,doe,str(vi),mark,amount]
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
                     fh=open("Youtubers.csv","r",newline='')
                     re=csv.reader(fh)
                     y=list(re)
                     fh.close()
                     print(" Choose what changes do you want  to make ")
                     print(" 1. To make any changes in the deal of  youtuber ") 
                     print(""" 2. To remove a particular youtuber's record from the database
                     (By selecting this option you will be able to delete the record of any one youtuber at a given chance) """)
                     print(" 3. Move back to previous menu")
                     Ch=int(input("Enter your choice number from the above options :"))
                     if Ch==1:
                            t=int(input(" Enter the number of youtuber's whose information you wanna change :"))
                            m=len(y)
                            for i in range(t):
                                   nam=input(" Enter the name of the youtuber whose information you wanna change :")
                                   for j in range(m):
                                          if y[j][0]==nam:
                                                 k=int(input("Enter the number of times you want to edit the records of this youtuber:"))
                                                 for s in range(k):
                                                        fh=open("Youtubers.csv","w",newline='')
                                                        wri=csv.writer(fh)
                                                        print("what do you want to change ?")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print(" 1. Change the name of the youtuber.")
                                                        print(" 2. Change the number of subscribers of the youtuber's YouTube channel.")
                                                        print(" 3. Change the date of start of contract.")
                                                        print(" 4. Change the date of end of contract.")
                                                        print(" 5. Change the average number of views per video")
                                                        print(" 6. Change the type of advertisement done by the Youtuber.")
                                                        print(" 7. Change the amount to be payed to the youtuber.")
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        print()
                                                        print()
                                                        print()
                                                        input("Press Enter")
                                                        cH=int(input("Enter your choice number from the above options :"))
                                                        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                                        if cH==1:
                                                               name=input(" enter the new name of the youtuber :")
                                                               y[j][0]=name
                                                        elif cH==2:
                                                               num=input(" enter the new number of subscribers of the youtuber :")
                                                               y[j][1]=num
                                                        elif cH==3:
                                                               dos=input(" enter the new date of start of contract of the youtuber :")
                                                               y[j][2]=dos
                                                        elif cH==4:
                                                               doe=input(" enter the new date of end of contract of the youtuber :")
                                                               y[j][3]=doe
                                                        elif cH==5:
                                                               avg=input(" enter the new average number of views per video of the youtuber :")
                                                               y[j][4]=avg
                                                        elif cH==6:
                                                               adv=input(" enter the new type of advertisement (skipable/non-skipable/in video) chosen by the youtuber :")
                                                               y[j][5]=adv
                                                        elif cH==7:
                                                               amt=input(" enter the new amount to be payed to the youtuber :")
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
                                          print(" Sorry youtuber with the entered name not found :(")
                                          print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                                          print()
                                          print()
                                          print()
                                          continue
                     elif Ch==2:
                            name=input(" Enter the name of the youtuber related to whom you want to delete the record :")
                            m=len(y)
                            for i in range(0,m):
                                   if y[i][0]==name:
                                          fh=open("Youtubers.csv","w",newline='')
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
                                   print(" Sorry youtuber with the entered name not found :(")
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
