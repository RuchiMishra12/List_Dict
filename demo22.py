#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 22
#"Marks of students are stored in a list.
#marks = [78, 35, 90, 40, 55]
#Write a program to:
#Print PASS if marks ≥ 40
#Print FAIL if marks < 40
#Count how many students passed"
marks=[78,35,90,40,55]
count=0
for i in marks:
 if i>=40:
    count+=1
    print("Pass") 
 else:
    print("Fail")
print("Passed students:",count)