#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 21
#"A small shop sells 5 items. You need to create a program that acts as a POS (Point of Sale) system.
#Tasks:
#The Database: Create a dictionary called menu where keys are item names (e.g., ""Samosa"", ""Tea"", ""Coffee"") and values are their prices.
#The Shopping List: Create an empty list called cart.
#The Input Loop: Use a while loop to ask the user to type an item name to add to their cart. Type ""done"" to stop.
#Validation: If the user types an item not in the menu, print ""Item not available.""
#The Bill: After ""done"" is typed, loop through the cart list. For each item, look up its price in the menu dictionary and calculate the total sum.
#Final Output: Print a ""Receipt"" showing the items bought and the final total price."
menu={"Samosa":10,"Tea":15,"Coffee":20}
cart=[]
sum=0
while True:
    user=input("ask your item:")
   
    if user in menu:
        cart.append(user)
    elif user=="done":
        print(cart) 
        break
    else:
            print("item is not found")
print("Recipt : ")
for key ,value in menu.items():
   if key in cart:
        sum+=value
        print(key,"=",value)
print("Tota Bill : ", sum)



         
            
       
       
    
        

    
        