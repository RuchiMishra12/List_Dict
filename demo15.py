#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 15
#A week's temperatures are stored in a list. Find how many days were "Hot" (above 35°C)
temperatures=["27°C","30°C","33°C","35°C","37°C","40°C","42°C"]
count=0
for i in temperatures:
    if i>"35°C":
       count+=1
print("Hot days:",count)

              