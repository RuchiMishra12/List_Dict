#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 13
#Create a list of ages. Create two new lists: minors (under 18) and adults (18 and above)
ages=[11,15,17,18,20,22]
minors=[]
adults=[]
for i in ages:
    if i<18:
        minors.append(i)
    else:
        adults.append(i)
print("minor list:",minors) 
print("adults list:",adults)     