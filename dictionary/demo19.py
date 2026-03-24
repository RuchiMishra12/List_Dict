#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 19
#"Create a simple phone book using a dictionary where name is the key and phone number is the value.
#Features
#Students should implement:9
#Add new contact
#Display all contacts
#Search contact by name
#Delete a contact"
dict={"Khushi":9076896505,"Kashish":9580119604,"Shaivi":7317851462,"Mansi":9026325411}
search=input("enter your name:")
for key,value in dict.items():
    if search==key:
        print(key,value)
dict.update({"Ruchi":7991864973})
print(dict)
dict.pop("Ruchi")
print(dict)