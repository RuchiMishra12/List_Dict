#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 18
#"Create a program to manage student marks using dictionary.
#Features
#Store student name and marks
#Display all students
#Search student
#Find topper
#Calculate class average"
student_marks={"Anya":50,"Zvya":70,"Sreeja":90}
search=input("search student name:")
sum=0
for i in student_marks.values():
    sum+=i
    average=sum/len(student_marks)
if search in student_marks:
    print("yes")
else:
    print("no")
#print(sum)
print(student_marks.keys())
print("topper:",max(student_marks,key=student_marks.get))
print("class average:",average)