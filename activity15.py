#odd summanation 

number = 0

for i in range (1,11,1):
    num = eval(input(('please enter a number :')))
    if num % 2 == 1:
        number += num

print(f"The sum off odd number is:{number}" )
         


