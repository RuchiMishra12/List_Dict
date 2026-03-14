#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 5
#Create a list of 10 random integers. Use a for loop to print each number multiplied by 2.
"""list=[2,28,4,8,52,14,54,20,22,26]
for i in range(len(list)):
  print(list[i]*2)"""
import random
n=[]
for count in range(1,11):
        temp=random.randrange(1,100)
        n.append(temp)
print(n)

        