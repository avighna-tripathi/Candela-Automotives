def view():
       while True:
              print(' You have chosen to view the sales manually ')
              import csv
              fh=open('sales.csv','r')
              csv_reader=csv.reader(fh)
              reader1=list(csv_reader)
              n=len(reader1)
              print(" How do you wish to view the records of sales ?")
              print(" 1. By year name .")
              print(" 2. By range of years .")
              print(" 3. Full Record .")
              print(" 4. Back to previous menu .")
              ch=int(input(' Enter your choice from the above options ? :'))
              if ch==1:
                     year=input('Enter the year name like:2015, etc :')
                     if int(year)<2015:
                            print("Can't display the records as the year entered is before 2015 and the company was founded in 2015")
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     elif int(year)>int(reader1[n-1][0]):
                            print(" Record of the given year does not exist yet in the database")
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     elif int(year)<int(reader1[n-1][0]) and int(year)>2015:
                            for i in range(n):
                                   if reader1[i][0]==year:
                                          print(reader1[0])
                                          print(reader1[i])
                                          break
                                   break
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
              elif ch==2:
                     year1=input(' Enter the starting year for viewing the records :')
                     year2=input(' Enter the ending year for viewing the records :')
                     i1,i2=0,0
                     for i in range(n):
                            if reader1[i][0]==year1:
                                   i1=i
                            elif reader1[i][0]==year2:
                                   i2=i       
                     if i1>=0 and i1<=n-2 and i2<=n-1 and i2>=1:
                            for j in range(i1,i2+1):
                                   print(reader1[0])
                                   print(reader1[j])
                                   print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     else:
                            print(' Out of range values for starting year or ending year or both ')
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     q=input(' Want to see more (YES/Anything(NO)) ?:')
                     if q=='YES':
                            continue
                     else:
                            print('Bye..............')
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            break
              elif ch==3:
                     for i in range(n):
                            print(reader1[i])
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
              elif ch==4:
                     print(' Thank you ')
                     print(' Returing to previous Menu ')
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     break
              else:
                     print(' Wrong choice Entered. Try Again ')
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
view()
