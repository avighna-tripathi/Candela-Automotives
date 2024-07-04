print('                                                                                       Welcome To The Plan Maintainance Department of Candela Automobiles')
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print()
print()
print('In this department the user/admin is allowed to view our stats i.e., profit for every year (since 2015), average yearly sales of our company,etc.')
print()
print()
print('Hope You will find it amazing while spending your time with us.')
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print()
print()
print()
print(' Here is the content of the menu which consists of the operations we allow you to perform')
print()
input('Press Enter')
print()
print()
print()
print()
print()
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
while True:
       print('1. To  add the sales of that year, profit in that year, Target sale amount, Target achieved(YES/NO/ALMOST),profit percentage (automatically calculated) in our database.')
       print('2. To view the statistics of our sales in normal format.')
       print('3. To view our stats in the form of bar graph.')
       print('4. Bact to previous Menu')
       Ch=int(input(' Enter your choice number from the above options yo:'))
       if Ch==1:
              import addsal
       elif Ch==2:
              import viewsal
       elif Ch==3:
              import grphsal
       elif Ch==4:
              print(' Thank you for visiting us. Hope to see You soon :)')
              break
       else:
              print(' Wrong choice Try again !!')
              continue
