#factorial program

num = eval(input("Enter a number: "))

number = num
result = 1
for x in range(num, 1, -1 ):
    result *= x

print("The factorial of", number, "is", result)