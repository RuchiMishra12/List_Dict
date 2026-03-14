#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 21
#"A teacher stores marks of students in a list
#marks = [78, 65, 89, 90, 56]
#Write a program to:
#Print all marks
#Find total marks
#Find average marks
#Find highest marks
#Find lowest marks"
marks=[78,65,89,90,56]
sum=0
for i in marks:
    sum+=i
    average=sum//5
print("all marks:",marks)
print("total marks:",sum)
print("average marks:",average)
marks.sort()
print(marks)
print("highest marks:",marks[-1])
print("lowest marks:",marks[0])