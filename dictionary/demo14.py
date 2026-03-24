#Programmed By : Ruchi Mishra
#Roll No : 55
#Dictionary assignment number : 14
#Create a dictionary inventory = {'Pens': 10, 'Erasers': 5}. Ask the user which item they bought and decrease that item's count by 1
inventory={'pens':10,'Erasers':5}
user=input("enter the item name:")
for key,value in inventory.items():
      if user==key:
         inventory[key] =value-1
print(inventory)