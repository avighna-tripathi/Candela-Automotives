import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
fh=open('sales.csv','r')
reader=csv.reader(fh)
reader1=list(reader)
n=len(reader1)
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(' How do you want to view the statistics of sales in bar graph format ?')
print('1. All records')
print('2. By year range')
print('3. Exit')
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
ch=int(input(' Enter your choice from the above options :'))
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print()
print()
if ch==1:
       while True:
              print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
              print(' How do you want to view all the records ?')
              print('1. Year ,sales in that year and target sales for that year.')
              print('2. Year and profit amount in that year')
              print('3. Year, sales in that year and profit in that year.')
              print('4. Year and profit percentage.')
              print('5. Exit')
              print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
              ch1=int(input(' Enter your choice from the above options :'))
              if ch1==1:
                     x1,y1,y2=[],[],[]
                     for i in range(1,n):
                            x1.append(int(reader1[i][0]))
                            y1.append(int(reader1[i][1]))
                            y2.append(int(reader1[i][4]))
                     x1_index=np.arange(len(x1)) 
                     width=0.2
                     plt.bar(x1_index,y1,width,color='red',edgecolor='pink',label='Sales')
                     plt.bar(x1_index+width,y2,width,color='green',edgecolor='pink',label='Target Sales')
                     plt.xticks(x1_index,x1)
                     plt.title('Bar Graph of Sales , Target sales for a Year',fontsize=17)
                     plt.xlabel('YEARS',fontsize=12,rotation=20)
                     plt.ylabel('IN MILLION $',fontsize=12)
                     plt.legend()
                     plt.show()
              elif ch1==2:
                     x1,y1=[],[]
                     for i in range(1,n):
                            x1.append(int(reader1[i][0]))
                            y1.append(int(reader1[i][2]))
                     width=0.4
                     plt.bar(x1,y1,width,color='orange',edgecolor='pink',label='Profit Amount')
                     plt.title('Bar Graph of profit in a year',fontsize=17)
                     plt.xlabel('YEARS',fontsize=12,rotation=20)
                     plt.ylabel('IN MILLION $',fontsize=12)
                     plt.legend()
                     plt.show()
              elif ch1==3:
                     x1,y1,y2=[],[],[]
                     for i in range(1,n):
                            x1.append(int(reader1[i][0]))
                            y1.append(int(reader1[i][1]))
                            y2.append(int(reader1[i][2]))
                     x1_index=np.arange(len(x1))
                     width=0.2
                     plt.bar(x1_index,y1,width,color='blue',edgecolor='pink',label='Sales')
                     plt.bar(x1_index+width,y2,width,color='purple',edgecolor='pink',label='Profit Amount')
                     plt.xticks(x1_index,x1)
                     plt.title('Bar Graph of Sales , Profit Amount in a year',fontsize=17)
                     plt.xlabel('YEARS',fontsize=12,rotation=20)
                     plt.ylabel('IN MILLION $',fontsize=12)
                     plt.legend()
                     plt.show()
              elif ch1==4:
                     x1,y1=[],[]
                     for i in range(1,n):
                            x1.append(int(reader1[i][0]))
                            y1.append(int(reader1[i][3]))
                     width=0.4
                     plt.bar(x1,y1,width,color='yellow',edgecolor='pink',label='Profit Percentage')
                     plt.title('Bar Graph of profit percentage in a year',fontsize=17)
                     plt.xlabel('YEARS',fontsize=12,rotation=20)
                     plt.ylabel('IN %',fontsize=12)
                     plt.legend()
                     plt.show()
              elif ch1==5:
                     print(' Come Again Soon.')
                     break
              else:
                     print('Wrong Input. Try Again')
elif ch==2:
       while True:
              x1=[]
              year1=input(' Enter the starting year for viewing the records :')
              year2=input(' Enter the ending year for viewing the records :')
              i1,i2=0,0
              
              for i in range(1,n):
                     if reader1[i][0]==year1:
                            i1=i
                            break
                     else:
                            print('Wrong input. Try Again')
                            break
              else:
                     print(' Starting year or ending year or both not in record. Try entering some other year')
                     break
              for j in range(1,n):
                     if reader1[j][0]==year2:
                            i2=j
                            break
                     else:
                            print('Wrong input. Try Again')
                            break
              else:
                     print(' Starting year or ending year or both not in record. TRy entering some other year')
                     break
              if i1>=1 and i1<=n-2 and i2<=n-1 and i2>=2:
                     for j in range(i1,i2+1):
                            x1.append(int(reader1[j][0]))
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     print(' How do you want to view all the records ?')
                     print('1. Year ,sales in that year and target sales for that year.')
                     print('2. Year and profit amount in that year')
                     print('3. Year, sales in that year and profit in that year.')
                     print('4. Year and profit percentage.')
                     print('5. Exit')
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     ch1=int(input(' Enter your choice from the above options :'))
                     if ch1==1:
                            y1,y2=[],[]
                            for j in range(i1,i2+1):
                                   y1.append(int(reader1[j][1]))
                                   y2.append(int(reader1[j][4]))
                            x1_index=np.arange(len(x1)) 
                            width=0.2
                            plt.bar(x1_index,y1,width,color='red',edgecolor='pink',label='Sales')
                            plt.bar(x1_index+width,y2,width,color='green',edgecolor='pink',label='Target Sales')
                            plt.xticks(x1_index,x1)
                            plt.title('Bar Graph of Sales , Target sales for a Year',fontsize=17)
                            plt.xlabel('YEARS',fontsize=12,rotation=20)
                            plt.ylabel('IN MILLION $',fontsize=12)
                            plt.legend()
                            plt.show()
                     elif ch1==2:
                            y1=[]
                            for j in range(i1,i2+1):
                                   y1.append(int(reader1[j][2]))
                            print(x1)
                            width=0.2
                            x1_index=np.arange(len(x1))
                            plt.bar(x1_index,y1,width,color='orange',edgecolor='pink',label='Profit Amount')
                            plt.xticks(x1_index,x1)
                            plt.title('Bar Graph of profit in a year',fontsize=17)
                            plt.xlabel('YEARS',fontsize=12,rotation=20)
                            plt.ylabel('IN MILLION $',fontsize=12)
                            plt.legend()
                            plt.show()
                     elif ch1==3:
                            y1,y2=[],[]
                            for j in range(i1,i2+1):
                                   y1.append(int(reader1[j][1]))
                                   y2.append(int(reader1[j][2]))
                            x1_index=np.arange(len(x1))
                            width=0.2
                            plt.bar(x1_index,y1,width,color='blue',edgecolor='pink',label='Sales')
                            plt.bar(x1_index+width,y2,width,color='purple',edgecolor='pink',label='Profit Amount')
                            plt.xticks(x1_index,x1)
                            plt.title('Bar Graph of Sales , Profit Amount in a year',fontsize=17)
                            plt.xlabel('YEARS',fontsize=12,rotation=20)
                            plt.ylabel('IN MILLION $',fontsize=12)
                            plt.legend()
                            plt.show()
                     elif ch1==4:
                            y1=[]
                            for j in range(i1,i2+1):
                                   y1.append(int(reader1[j][3]))
                            width=0.4
                            x1_index=np.arange(len(x1))
                            plt.bar(x1_index,y1,width,color='yellow',edgecolor='pink',label='Profit Percentage')
                            plt.xticks(x1_index,x1)
                            plt.title('Bar Graph of profit percentage in a year',fontsize=17)
                            plt.xlabel('YEARS',fontsize=12,rotation=20)
                            plt.ylabel('IN %',fontsize=12)
                            plt.legend()
                            plt.show()
                     elif ch1==5:
                            print(' Come Again Soon.')
                            break
                     else:
                            print('Wrong Input. Try Again')
elif ch==3:
       print(' See you soon. ')
else:
       print(' Wrong Input ')
