#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 15
#Given a dictionary of employees and their salaries, increase every salary by 10% and update the dictionary
employees={"Anya":1000,"Avika":2000,"Sreeja":3000}
for key,value in employees.items():
   employees[key]=value+value*10/100
print("updated: ",employees)       

