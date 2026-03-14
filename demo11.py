#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 11
#Take a list like [-5, 3, -2, 8]. Create a new list where all negative numbers are converted to positive.
list=[-5,3,-2,8]
new_list=[]
for i in list:
    if i>0:
        new_list.append(i)
    else:
        i*=-1
        new_list.append(i)
print(new_list)