def bill(dest):
    rate=dest*5
    print("cost of per kilometer is Rs.5\n ur cost to destination is ",rate)
a=int(input("Enter ur destination From poonamalle \n1.Avadi \n2.Ambattur \n3.Redhills\n"))
if(a==1):
    bill(10)
elif(a==2):
    bill(20)
elif(a==3):
    bill(35)
else:
    print("incorrect destination")

'''
sample input & output
Enter ur destination From poonamalle 
1.Avadi 
2.Ambattur 
3.Redhills
1
cost of per kilometer is Rs.5
 ur cost to destination is  50
>>> 
sample input & output
Enter ur destination From poonamalle 
1.Avadi 
2.Ambattur 
3.Redhills
3
cost of per kilometer is Rs.5
 ur cost to destination is  175
>>> 

'''
