print("Basics")
for x in range (0,151):
    print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Multiples of 5")
for x in range (5,1001,5):
    print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Counting the Dojo Way")
for x in range(1, 101):
    if (x%10==0):
        print("Coding Dojo")
    elif (x%5==0):
        print("Coding")
    else:
        print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Whoa. That sucker's huge.")
i=1
sum=0
while i<=500001:
    if i%2!=0:
        sum=sum+i
    i=i+1
print("Sum of odd numbers",sum)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Countdown by Fours")
for x in range(2018,1,-4):
    print(x)

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Flexible Counter")
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum,highNum):
    if x%3 == 0:
        print(x)
