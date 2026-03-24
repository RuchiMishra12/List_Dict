#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 16
#Allow a user to input a name and a phone number via input() and store it in a dictionary until they type "exit".
"""store={}
while True:
     n=input("enter name : ")
     if n=="exit":
          break
     mobile=int(input("enter mobile number : "))
     store[n]=mobile
print(store)"""

store={}
while True:
    n=input("enter name:")
    if n=="exit":
        break
    mobile=int(input("enter your mobile number:"))
    store[n]=mobile
print(store)
