#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 14
#Store prices of 5 items in a list. Calculate the total bill and the average price per item.
Price=[100,200,300,400,500]
sum=0
for i in Price:
    sum+=i
    average=sum//5
print("Total Bill:",sum)
print("average:",average)