import csv
fh=open('sales.csv','r')
reader=csv.reader(fh)
reader1=list(reader)
fh.close()
n=len(reader1)
fh1=open('sales.csv','a',newline='')
wri=csv.writer(fh1)
while True:
       year=input("Enter The Year in which the sales' record you wanna enter :")
       for j in range(1,n):
              if reader1[j][0]==year:
                     print("The record of the entered year already exist. Try Again and don't enter any year between 2015-2020")
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     break
              elif int(year)<2015:
                     print(" Sorry any year before 2015 is not eligible because the company was founded in 2015 only. Try Again")
                     print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                     break
              continue
       else:
              sal=int(input('Enter the sales (in million $) :'))
              pro=int(input('Enter the profit (in million $):'))
              prof=(pro/sal)*100
              tar='0'
              if sal-pro==0:
                     tar='YES'
              elif sal-pro>0 and sal-pro<50:
                     tar='ALMOST'
              else:
                     tar='NO'
              wri.writerow([year,str(sal),str(pro),str(prof),tar])
              print(' Record Entered Successfully ')
              print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
       ch=input(' Do you wish to enter more records (YES/NO , enter in uppercase only) ?')
       if ch=='YES':
              continue
       else:
              print('Moving Back to previous Menu')
              print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
              break
fh1.close()
       
