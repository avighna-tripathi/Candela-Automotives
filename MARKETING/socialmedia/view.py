import csv

def view():                                                            #coding to view the stats of social media influencers
       while True:
              print('How do you want to view the statistics ?')
              print(' 1. All Records at once.')
              print(' 2. By the name of each influencer.')
              print(' 3. Back to previous menu')
              print()
              print()
              print()
              print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
              input("Press Enter")
              choice=int(input(' Enter the choice number from the above options :'))
              if choice==1:
                     file=open('socmed.csv','r')
                     reader1_csv=csv.reader(file)
                     reader1=list(reader1_csv)
                     i=len(reader1)
                     for j in range(0,i):
                            k=reader1[j]
                            print(k)
                     print()
                     print()
                     print()
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     input("Press Enter")
                     file.close()
              elif choice==2:
                     file=open('socmed.csv','r')
                     reader2_csv=csv.reader(file)
                     reader2=list(reader2_csv)
                     l=reader2[0]
                     reader2.remove(l)
                     i=len(reader2)
                     name=input("Enter the name of the influencer whose information and deal you want to view :")
                     for j in range(0,i):
                            if reader2[j][0]==name:
                                   t=reader2[j]
                                   print(l)
                                   print(t)
                                   break
                     else:
                            print(" Record related to the entered influencer's name not found!!!")
                     print()
                     print()
                     print()
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     file.close()
                     input("Press Enter")
              elif choice==3:
                     print()
                     print()
                     print()
                     print(' Thank you :))')
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     input("Press Enter")
                     break
              else:
                     print(" Wrong option Try again ")
                     print()
                     print()
                     print()
                     print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                     input("Press Enter")
view()
