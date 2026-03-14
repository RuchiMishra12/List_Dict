#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 10
#Given a list of 10 student marks, count how many students scored above 40.
student_marks=[10,20,25,30,35,40,50,60,70,80]
count=0
for i in student_marks:
  if  i>=40:
    count=count+1
print(count)