#odd number summation 
print("enter a 10 numbers")

sum = 0
for x in range(10):
    num = eval(input("Enter a number: "))
    if num % 2 != 0:
        sum += num
print("The sum of the odd numbers is", sum)  