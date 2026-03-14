#Programmed By : Ruchi Mishra
#Roll No : 55
#List assignment number : 23
#"A cricket player scored runs in 6 matches.
#Example: [45, 60, 10, 80, 55, 90]s
#Write a program to:
#Find total runs
#Find highest score
#Count how many matches player scored more than 50 runs"
scored=[45,60,10,80,55,90]
sum=0
count=0
for i in scored:
    if i>50:
      count+=1
      sum+=i
print("total runs:",sum)
scored.sort()
print(scored)
print("highest score:",scored[-1])
print("Player score more than 50:",count)