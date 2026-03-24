#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 10
#Given a dictionary of student names and their marks, print only the names of students who scored above 75
dict={"Anya":90,"Avya":80,"sreeja":75,"Sanvi":60,"Manvi":70}
for key,value in dict.items():
    if value>75:
        print(key)