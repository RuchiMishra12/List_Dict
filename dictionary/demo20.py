#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 20
#"Create Attendance System where 
#Faculty should:
#Add attendance for 5 students
#Count total present students
#Display absent students"
students="Khushi","Ruhi","Priya","Sandhya","Shaivi"
attendence=1,0,1,0,1
present=0
absent=0
#p=[]
b=[]
a=dict(zip(students,attendence))
print(a)
for key,value in a.items():
    if value==1:
         present+=1
         
    else:
        value==0
        absent+=1
        b.append(key)
        c=",".join(b)+" "
print("Count total present students : ",present)
print("Display absent students : ",absent,c)