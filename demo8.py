#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 8
#Given a list of numbers 1-20, create a new list that contains only the even numbers.
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
new_list=[]
for i in range(len(numbers)):
    if i%2==0:
     new_list.append(i)
print(new_list)