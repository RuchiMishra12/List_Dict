#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 19
#"A teacher stored attendance of students in a list (1 = present, 0 = absent).
#Example: [1,1,0,1,0,1,1]
#Write a program to:
#Count total present
#Count total absent
#Print attendance percentage"
attendence=[1,1,0,1,0,1,1]
pcount=0
acount=0
for i in attendence:
    if i==1:
       pcount+=1
    elif i==0:
         acount+=1
attendence_percentage=pcount/len(attendence)*100
print("total present:",pcount)
print("total absent:",acount)
print("total attendence percentage:",attendence_percentage)