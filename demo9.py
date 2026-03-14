#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 9
#Write a program that takes a list of names and a "search_name" from the user. Print the index where the name is found, or "Not Found."
names=["Ruchi","Khushi","Kashish","Shaivi","Mansi"]
search_name=input("enter name:")
if search_name in names:
        print("found",names.index(search_name))
else:
        print("not found")