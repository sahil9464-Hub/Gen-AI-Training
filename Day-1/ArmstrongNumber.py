# Armstrong Number

num = int(input("Enter a number: "))

sum = 0
temp = num

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
