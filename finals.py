import os
from Compile import *
Library = True
challenge = True 
    
print('Welcome to My Programming Compilation (Using Python)  ')
print('_______________________________________________________')

N = input('Enter your given name --> ')
os.system('cls')

print(f'Hi {N}, Welcome to my Phyton Program library\n'
       'I\'m Drake Cruz\nFrom BSIT-1A'
    )    

while Library == True:
    print('_______________________________________________________')

    print('     | [ First Semester  Python Program ] |\n'
        '     |         [ Activity list ]          |\n'
        '     |                                    |\n'
        '     |     (1) Printing Programs          |\n'
        '     |     (2) Computing Programs         |\n'
        '     |     (3) T/F statement Program      |\n'
        '     |     (4) IF condition Program       |\n'
        '     |     (5) Forloop Program            |\n'
        '     |     (6) Nested Forloop Program     |\n'
        '     |     (7) While loop Program         |\n'
        '     |     (8) Listing Program            |\n'
        '     |     (9) Def function Program       |\n'
        '     |                                    |\n'
        '_______________________________________________________\n'
        'Enter the Number of Program you want to Open\n\n'
        '(X) Close Program\n'
        '(N) Next Page\n'
    )

    Choice = input('Enter Input here --> ').lower()
    os.system('cls')

    if Choice  == '1':
        print('        [ Printing Programs ]')
        print('____________________________________________\n\n'
            '   | (1) My First program               |\n'
            '   | (2) Printing My info               |\n'
            '   | (3) Printing with string Function  |\n\n'
            '____________________________________________\n'
            '(X) Close\n'
        )
        Choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if Choice == '1':
            print('        [ The code of the program ]\n'
                '____________________________________________\n\n'
                '   \"This is My first Program a Simple Hello\"\n         \"To world of Programming.\"\n\n'
                '   print("Hello World")\n'
                '____________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')  

            if run == 'yes':
                act1()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '2':
            print( '             [ The code of the Program ]\n'
                '______________________________________________________\n\n'
                '   This is my Printing program with my basic Info\n'
                '   n = "Drake Cruz"\n'
                '   a = "19"\n'
                '   f = "BSIT 1-A"\n'
                '   y = "1st Year"\n\n'
                '   print("Name :", n)\n'
                '   print("Age :", a)\n'
                '   print("Section :", f)\n\n'
                '   print("Year :", y)\n\n'
                '______________________________________________________\n\n'
            )
            run = input('   Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act2()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
                
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif Choice == '3':
            print('        [ The code of the Program ]\n'
            '______________________________________________________\n\n'
            'print ("GOOD MORNING \n HI!!!! \n \t\t Happy birthday!! ")\n\n'
            '______________________________________________________\n\n'
            )

            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act3()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '2':
        print('          [Computing Programs]')
        print('_______________________________________\n\n'
            '   |    (1) Letter Counter        |\n'
            '   |    (2) Data type function    |\n'
            '   |    (3) Calculator            |\n'
            '   |    (4) Assignment Operator   |\n'
            '_______________________________________\n'
            '(X) Exit\n'
        )
        Choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if Choice == '1':
            print('         [ The code of the Program ]\n'
                '_________________________________________________\n\n'
                '   name = input(\"Enter a String -> \")\n'
                '   print(\"Your name has, len(name), characters\")\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act4()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '2':
            print('           [ The code of the Program ]')
            print('_________________________________________________\n\n'
                '   something = eval(input(\" Your Input =  \"))\n\n'

                '   print(\" The Data Type is, type(something) \")\n\n'

                '   answer = 6 + something\n\n'

                '   print(\" the answere is = \", answer)\n\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act5()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '3':
            print('            [ The code of the Program ]')
            print('_________________________________________________\n\n'
                '   n1 = eval(input("Enter Your First Numer ="))\n'
                '   n2 = eval(input("Enter Your First Number ="))\n\n'

                '   s = n1 + n2\n'
                '   d = n1 - n2\n'
                '   p = n1 * n2\n'
                '   q = n1 / n2\n'

                '   print("\nThe sum of", n1,"and", n2,"is", s)\n'
                '   print("the difference of", n1,"and", n2,"is", d)\n'
                '   print("The product of", n1,"and", n2,"is", p)\n'
                '   print(n1,"exponent by", n2,"is", n1**n2)\n'
                '   print("the remainder of", n1,"and", n2,"is", n1 % n2)\n'
                '   print("the floor division of", n1,"and", n2,"is", n1//n2)\n\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act6()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '4':
            print('          [ The code of the Program ]')
            print('_________________________________________________\n\n'
                '       a = 6\n'
                '               '
                '       a += 2\n'
                '       a *= 3\n'
                '       a += 9\n'
                '       a -= 5\n'
                '       a /= 7\n\n'

                '       print("the value of a is ", a)\n\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act7()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '3':
        print('[ Programs Using T/F Statements ]\n'
            '_________________________________________________\n\n'
            '   |      (1) Value comparison      |\n'
            '   |                                         |\n'
            '   |      (2) Name and Pass                  |\n\n'
            '_________________________________________________\n'
            '(X) Exit\n'
            
        )
        choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choice == '1':
            print('           [ The code of the Program ]\n'
                 '_________________________________________________\n\n'
                 '         bal = 500\n'
                 '         wit = 250\n\n'

                 '         print(balance < withdrawal)\n\n'

                 '         a = 3\n'
                 '         b = 2\n\n'
                 '         print(a > b)\n'
                 '_________________________________________________\n\n'
            )

            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act8()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif choice == '2':
            print('               [ The code of the Program ]\n'
                 '___________________________________________________________\n\n'
                 '      username = YungD\n'
                 '      password = highestamongtherest\n\n'

                 ' print(username == YungD)\n'
                 ' print((username == YungD) and (password == highestamongtherest))\n'
                 ' print((username == YungD) or (password == highestamongtherest))\n'
                 ' print (not((username == YungD) or (password == highestamongtherest)))\n'
                 '___________________________________________________________\n\n'
            )

            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act9()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '4':
        print('        [ Programs Using IF condition ]\n'
              '_______________________________________________\n\n'
              '     |     (1) Student Fare Discount      |\n'
              '     |     (2) Temperature Reader         |\n'
              '_______________________________________________\n'
              '(X) Exit\n'
        )
        choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choice == '1':
            print('                 [ The code of the Program ]\n'
                  '________________________________________________________________\n\n'
                  '     a = input(Pls Input Your Name -->)\n'
                  '     b = input("Are you a student? (YES/NO)-->").lower()\n'
                  '     c = eval(input("Input Fare -->"))\n\n'

                  '     if b == "yes":\n\n'

                  '        discount = fare * .2\n'
                  '        print("Hi", name, " student discount is ", discount )\n\n'

                  '     else :\n'
                  '         print("Sorry", name, "you are not eligible for discount")\n'
                  '________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act10()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        if choice == '2':
            print('                 [ The code of the Program]\n'
                  '________________________________________________________________\n\n'
                  '     print("Temperature Reader")\n\n'

                  '       temp = input("Pls Input Temperature --> ")\n\n'
                  '       if a <= "0":\n'
                  '         print("the temperature is super cold")\n\n'
                  '       elif temp >= 1 and temp <= 20:\n'
                  '         print("Temperature is Cold")\n\n'
                  '       elif temp >= 21 and temp <= 30:\n'
                  '         print("the temperature is lukewarm")\n\n'
                  '       elif temp >= 31 and temp <= 40\n'
                  '         print("the temperature is warm")\n\n'
                  '       elif temp >= 41 and temp <= 50:\n'
                  '         print("the temperature is hot")\n\n'
                  '       elif temp >= 51:\n'
                  '         print("the temperature is boiling hot")\n\n'
                  '       else:\n'
                  '         print("invalid Temperature")\n\n'
                  '________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act11()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '5':
        print('[ Programs Using For Loop ]\n'
            '__________________________________________________\n\n'
            '   |      (1) Printing Text Using For Loop    |\n'
            '   |      (2) Adding using forloop            |\n'
            '   |      (3) Reverse Counting Loop           |\n'
            '   |      (4) Summation For loop              |\n'
            '   |      (5) Multiplication Table            |\n\n'
            '__________________________________________________\n\n'
            ' (X) Exit\n'
        )
        chosen = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if chosen == '1':
            print('            [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '           for ikot in range (1, 10, 1):\n'
	            '               print(ikot, "Hello World!!") \n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act12()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
            
        elif chosen =='2':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '       num = 0 \n\n'

	            '       for i in range (1, 11, 1):\n'
		        '       number = eval(input ("please enter a number:"))\n'
		        '       num += number\n'

	            '       print ("the sum of the number is ":, num)\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act13()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif chosen == '3':
            print('         [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '       for i in range (20, 1, -1):\n'
		        '       print(i, "Hello everyone")\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act14()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif chosen == '4':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '   number = 0\n\n'
                '   for me in range(1,11):\n\n'
                '   num = eval(input(("please enter a number" :)))\n\n'
                '   if num % 2 == 1:\n\n'
                '   number += num\n\n'
                '   print(f"The sum of odd number is: {number}")\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act15()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif chosen == '5':
            print('           [ The code of the Program ]\n'
                 '__________________________________________________\n\n'
                 '      for x in range(1,11,1):\n\n'

                 '        for j in range(1, 11, 1 ):'

                 '              print(j,end="")\n\n'

                 '      print()\n\n'
                 '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act16()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '6':
        print('        [ Programs Using Nested Loop ]\n'
              '_____________________________________________\n\n'
              ' |        (1) Triangle of *                 |\n'
              ' |        (2) Diamond of  *                 |\n'
              ' |        (3) Left Triangle of *            |\n'
              ' |        (4) Square of *                   |\n\n'
              '_____________________________________________\n\n'
              '(X) Exit'
        )

        choose = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choose == '1':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '   a = int(input("Input Howmany lines of * -->"))\n\n'
                'for i in range(1, a + 1):'
                '   print(" " * (a - i), end="")'

                '   for x in range(0, i):'
                '       print(i, end=(" "))'
                'print(" ")'           
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act17()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose == '2':
            print('            [ The code of the Program ]\n'
                  '__________________________________________________\n\n'
                  '     for i in range(1,11,1):\n'
                  '         for x in range(10,i,-1):\n'
                  '             print( " ",end=" ")\n'
                  '         for b in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '         for c in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '             print()\n\n'
                  '     for i in range(10,1,-1):\n'
                  '         for x in range(10,i,-1):\n'
                  '             print( " ",end=" ")\n'
                  '         for b in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '         for c in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '             print()\n\n'
                  '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act18()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose == '3':
            print('           [ The code of the Program ]\n\n'
                  '__________________________________________________\n\n'
                  '         for u in range(1,11, 1):\n\n'
                  '             for x in range(1,i,1):\n\n'
                  '             print("*",end=" ")\n\n'
                  '         print()\n'
                  '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act19()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif choose == '4':
            print('           [ The code of the Program ]\n'
                  '__________________________________________________\n\n'
                  '         for u in range(1,11, 1):\n\n'
                  '            for i in range(10,i,-1):\n\n'
                  '            print("*",end=" ")\n\n'
                  '            print()\n'
                  '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act20()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
    elif Choice == '7':
        print('        [Programs Using While Loops]\n'
              '_____________________________________________\n\n'
              '|      (1) Washing Machine                  |\n'
              '|      (2) Number Guessing Game             |\n'
              '_____________________________________________\n\n'
              '(X) Exit\n'
        )

        choose = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choose =='1':
            print('               [ The code of the Program ]\n'
                  '____________________________________________________________\n\n'
                  '     isDirty = True\n\n'
                  '     while isDirty == True:\n'
                  '     a = input("Continue The Cycle? (yes/no) --> ").lower()\n\n'
                  '     if a == "yes":\n'
                  '         print("The cycle continue :>")\n'
                  '         continue\n\n'
                  '     elif a == "no":\n'
                  '         print("The cycle stops :<")\n'
                  '         break\n\n'
                  '     else:\n'
                  '         print("Invalid Input ??")\n'
                  '         continue\n'
                  '____________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act21()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose =='2':
            print('             [ The code of the Program ]\n'
                  '_______________________________________________________\n\n'
                  '     import random\n\n'
    
                  '     num = random.randint(1,10)\n\n'

                  '     tries = 0\n'
                  '     we = True\n\n'

                  '     while we == True:\n'
                  '         g = int(input("What number u guess(1-10): "))\n'
                  '         tries += 1\n\n'

                  '         if g == num:\n'
                  '             print("Congratulation")\n'
                  '             print(f the number is num)\n'
                  '             print(f"YOu online took [tries] tries")\n'
                  '             break\n\n'

                  '         else:\n'
                  '             print("youre wrong")\n'
                  '             continue\n'
                  '_______________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act22()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '8':
        print('            [ Program Using Listing ]\n'
              '_____________________________________________\n\n'
              '|         (1) Listing Months in a Year      |\n'
              '_____________________________________________\n\n'
              'X = Exit\n\n '
        )
        choose = input('Enter the number of the program you want to open\n ----> ').lower()
        os.system('cls')

        if choose == '1':
            print('[ The code of the Program ]\n'
                  '_____________________________________________________\n\n'
                  '     months =[jan,feb,mar,april,may,june,jul]\n\n'

                  '         months.append(Aug)\n'
                  '         print(months)\n'
                  '         months.pop()\n'
                  '         print(months)\n'
                  '         months.append(Aug)\n'
                  '         print(months)\n'
                  '         months.reverse()\n'
                  '         print(months)\n\n'

                  '         for m in months:\n'
                  '             print(f \'m 2025\')\n\n'

                  '         fullname = \'CJ Sumagop\'\n\n'

                  '         for i in fullname:\n'
                  '             print(i)\n\n'

                  '         for c in fullname[::-1]:\n'
                  '             print(c)\n\n'

                  '         anthr = list(fullname)\n'
                  '             print(anthr)\n'
                  '         anthr.reverse()\n'
                  '             print(anthr)\n'
                  '_____________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act23()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
    
    elif Choice =='9':
        print('      [ Programs Using Def function ]\n'
              '_________________________________________\n\n'
              '|    (1) Printing & Calculator          |\n'
              '|    (2) Printing with def function     |\n'
              '|    (3) Printing from a List           |\n'
              '|    (4) Dictionary                     |\n'
              '_________________________________________\n\n'
        )
        choose = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choose =='1':
            print('            [ The code of the Program ]\n'
                  '___________________________________________________\n\n'
                  '     def food(a):\n'
                  '     print(f\'I want to eat [a]\')\n\n'
                  '     def number(c):\n'
                  '     a = 0\n\n'
                  '     for i in range(c, 0, -1):\n'
                  '     a += i\n\n'
                  '     print(f\'The sum of [c] is [a]\')\n\n'
                  '     def multiple(b):\n'
                  '     mult = 1\n'
                  '     for i in range(b, 0, -1):\n'
                  '     mult *= i\n'
                  '     return mult\n'
                  '     print(f\'the factorial of 5 is {multiple(5)}\')\n\n'
                  '     Act24_1\n'
                  '     from Act24 import food, number\n\n'

                  '     food(\'Sisig\')\n'
                  '     food(\'Pares\')\n\n'

                  '     number(10)\n'
                  '     number(15)\n'
                  '___________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act241()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose == '2':
            print('                   [ The code of the Program ]\n'
                  '__________________________________________________________________\n\n'
                  '     def Act21():\n'
                  '     a = 5\n'
                  '     print(\'The value of a is\', a)\n\n'

                  '     def Act22():\n'
                  '     a = 59\n'
                  '     print(\'The value of a is\', a)\n\n'

                  '     def Act23():\n'
                  '     a = 32923\n'
                  '     print(\'The value of a is\', a)\n\n'

                  '     from Act25 import Act21, Act22, Act23\n\n'

                  '     Act25_1\n'
                  '     isContinue = True\n\n'

                  '     while isContinue == True:\n'
                  '         print(\'Choose Program you want to open\')\n'
                  '         print(\'A - Act1 B - Act2 C - Act3 E - exit\')\n\n'

                  '     choose = input(\'What Program you want to open --> \').lower()\n\n'

                  '     if choose == "a":\n'
                  '         activity21()\n'
                  '         pass\n'
                  '         continue\n'
                  '     elif choose == \'b\':\n'
                  '         activtiy22()\n'
                  '         pass\n'
                  '         continue\n'
                  '     elif choose == \'c\':\n'
                  '         activity23()\n'
                  '         pass\n'
                  '         continue\n'
                  '     elif choose == "e":\n'
                  '         break\n'
                  '__________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act251()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif choose == '3':
            print('                 [ The code of the Program ]\n'
                  '__________________________________________________________________\n\n'
                  '   prutas = ["apple","mango","grapes"]\n\n'
                  '   prutas_kulay = {"red":"apple","yellow":"mango","violet":"grapes"}\n\n'
                  '   print(prutas_kulay.get("red"))\n'
                  '__________________________________________________________________\n\n'
            
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                act26()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif choose == '4':
            print('                          [ The code of the Program ]\n'
                  '_____________________________________________________________________________\n\n'
                  ' print(\'Adding data to Dictionary \')\n'
                  ' print(\'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\')\n\n'

                  ' Tuloy = True\n'
                  ' empty_dictionary = []\n\n'

                  ' while Tuloy == True:\n'
                  '     a = input(\'Enter Key for this Anime --> \')\n'
                  '     b = input(\'Enter Title of the Anime --> \')\n\n'

                  'empty_dictionary[a] = b\n\n'

                  'def print_anime():\n'
                  '     for i, a in empty_dictionary.items():\n'
                  '     print(f\'| Code --> [i] | Title --> [a] |\')\n'
                  'def search(key):\n'
                  '     print (\'search ....\')\n'
                  '     print(f\'result shows {empty_dictionary[key].upper() } on our Data base\')\n\n'

                  'c = input(\'Would you like to continue ?\n   Y - Yes\n   N - No\n   S - Search\n   P - Print --> \').lower()\n\n'

                  'if c == \'y\':\n'
                  '     print(\'Continuing ...\')\n'
                  '     continue\n'
                  'elif c == \'n\':\n'
                  '     print(\'program stops\')\n'
                  '     break\n'
                  'elif c == \'p\':\n'
                  '     print_anime()\n'
                  'elif c == \'s\':\n'
                  '     code = input(\'Input The book key --> \')\n'
                  '     search(code)\n'
                  '     continue\n'
                  'else :\n'
                  '     print(\'invalid Input \')\n'
                  '     continue\n'
                  '_____________________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run =='yes':
                act27()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == 'n':
        while challenge == True:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('     | [ First Semester  Python Program ] |\n'
                      '     |      [ Code challenge list ]       |\n'
                      '     |                                    |\n'
                      '     |     (1) Name Inside Diamond        |\n'
                      '     |     (2) Money Separator            |\n'
                      '     |     (3) Simple Log in              |\n'
                      '     |     (4) Even / Odd detector        |\n'
                      '     |     (5) Mangga Recommender         |\n'
                      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                      'Enter the Number of Program you want to Open\n\n'
                      '(R) Return First Page\n'
                )
                choice = input('Enter input here --> ').lower()
                os.system('cls')

                if choice == '1':
                    print('       [ The code of the Program ]\n'
                          '________________________________________\n\n'
                          'a = input(\"WHAT\'S YOUR NAME :\")\n'

                          'print("\\t\\t\\t\\t\\t",  a, "\\n\\t\\t\\t\\t\\t * \\n \\t\\t\\t\\t * \\t\\t * \\n \\t\\t\\t * \\t\\t\\t\\t * \\n \\t\\t * \\t\\t\\t HI\\t\\t\\t * \\n \\t * \\t\\t\\t\\t", a, "\\t\\t\\t\\t * \\n \\t\\t * \\t\\t\\t\\t\\t\\t *\\n \\t\\t\\t * \\t\\t\\t\\t *\\n \\t\\t\\t\\t * \\t\\t *\\n \\t\\t\\t\\t\\t *\\n")\n'
                          '________________________________________\n\n'
                        )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC1()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                    else:
                        print('Invalid Input')
                        os.system('cls')
                        continue
                
                elif choice == '2':
                    print('         [ The code of the Program ]\n'
                          '_____________________________________________\n\n'
                          '     amount = eval(input("Enter Amount: ₱"))\n\n'
                          '     k1 = int(amount // 1000)\n'
                          '     amount = amount - (k1 * 1000)\n\n'

                          '     h5 = int(amount // 500)\n'
                          '     amount = amount - (h5 * 500)\n\n'

                          '     h2 = int(amount // 200)\n'
                          '     amount = amount - (h2 * 200)\n\n'

                          '     h1 = int(amount // 100)\n'
                          '     amount = amount - (h1 * 100)\n\n'

                          '     p5 = int(amount // 50)\n'
                          '     amount = amount - (p5 * 50)\n\n'

                          '     p2 = int(amount // 20)\n'
                          '     amount = amount - (p2 * 20)\n\n'

                          '     p1 = int(amount // 10)\n'
                          '     amount = amount - (p1 * 10)\n\n'

                          '     c5 = int(amount // 5)\n'
                          '     amount = amount - (c5 * 5)\n\n'

                          '     c1 = int(amount // 1)\n'
                          '     amount = amount - (c1 * 1)\n\n'


                          '     print("₱1000 x ", str(k1))\n'
                          '     print("₱500  x ", str(h5))\n'
                          '     print("₱200  x ", str(h2))\n'
                          '     print("₱100  x ", str(h1))\n'
                          '     print("₱50   x ", str(p5))\n'
                          '     print("₱20   x ", str(p2))\n'
                          '     print("₱10   x ", str(p1))\n'
                          '     print("₱5    x ", str(c5))\n'
                          '     print("₱1    x ", str(c1))\n'
                          '_____________________________________________\n\n'
                          )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC2()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                    else:
                        print('Invalid Input')
                        os.system('cls')
                        continue

                elif choice == '3':
                    print('    [ The code of the Program ]\n'
                          '___________________________________\n\n'
                          '  user = "CJSumagop"\n'
                          '  pas = "POGIeh"\n\n'

                          '  a = input("ENTER YOUR USERNAME --> ")\n'
                          '  b = input("ENTER YOUR PASWORD --> ")\n\n'

                          '  if a == user and b == pas:\n'
                          '     print(\"Access Granted\")\n\n'  

                          '  else:\n'
                          '     print(\"Access denied\")\n'
                          '___________________________________\n\n'
                    )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC3()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                elif choice == '4':
                    print('         [ The code of the Program ]\n'
                          '____________________________________________\n\n'
                          '  num = eval(input("Enter a Number : "))\n\n'

                          '  num = num % 2\n\n'

                          '  if num == 0:\n'
                          '     print("Even Number")\n'
                          '  else:\n'
                          '     print("Odd Number")\n'
                          '____________________________________________\n\n'
                    )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC4()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                
                elif choice == '5':
                    print('[ The code of the Program ]\n')
                    print('''print("Welcome to Manga Read Recomendations")

                        name = input("Enter your name: ")
    print("Welcome to the Manga Reader Recommender", name, "!!!")
    print("\n!AVAILABLE GENRES!\n'action - romance - horror'")

    genre_choice = input("Please input genre type: ")

    if genre_choice.lower() == "action":
        print("You have selected Action")
        time = input("What year (2000s, 2010s): ")

        if time == "2000s":
            short_medium_long = input("How long should the manga be? (short, medium, long): ")

            if short_medium_long.lower() == "short":
                print("Recommendation: 'Black Lagoon'")
            else:
                if short_medium_long.lower() == "medium":
                    print("Recommendation: 'Fullmetal Alchemist'")
                else:
                    if short_medium_long.lower() == "long":
                        print("Recommendation: 'Naruto'")

        else:
            if time == "2010s":
                short_medium_long = input("How long should the manga be? (short, medium, long): ")

                if short_medium_long.lower() == "short":
                    print("Recommendation: 'One Punch Man'")
                else:
                    if short_medium_long.lower() == "medium":
                        print("Recommendation: 'Attack on Titan'")
                    else:
                        if short_medium_long.lower() == "long":
                            print("Recommendation: 'My Hero Academia'")

    else:
        if genre_choice.lower() == "romance":
            print("You have selected Romance")
            time = input("What year (2000s, 2010s): ")

            if time == "2000s":
                short_medium_long = input("How long should the manga be? (short, medium, long): ")

                if short_medium_long.lower() == "short":
                    print("Recommendation: 'Orange'")
                else:
                    if short_medium_long.lower() == "medium":
                        print("Recommendation: 'Strobe Edge'")
                    else:
                        if short_medium_long.lower() == "long":
                            print("Recommendation: 'Kimi ni Todoke'")

            else:
                if time == "2010s":
                    short_medium_long = input("How long should the manga be? (short, medium, long): ")

                    if short_medium_long.lower() == "short":
                        print("Recommendation: 'Ore Monogatari!! (My Love Story!!)'")
                    else:
                        if short_medium_long.lower() == "medium":
                            print("Recommendation: 'Ao Haru Ride (Blue Spring Ride)'")
                        else:
                            if short_medium_long.lower() == "long":
                                print("Recommendation: 'L♥DK'")

        else:
            if genre_choice.lower() == "horror":
                print("You have selected Horror")
                time = input("What year (2000s, 2010s): ")

                if time == "2000s":
                    short_medium_long = input("How long should the manga be? (short, medium, long): ")

                    if short_medium_long.lower() == "short":
                        print("Recommendation: 'The Drifting Classroom'")
                    else:
                        if short_medium_long.lower() == "medium":
                            print("Recommendation: 'Goth'")
                        else:
                            if short_medium_long.lower() == "long":
                                print("Recommendation: 'Hellsing'")

                else:
                    if time == "2010s":
                        short_medium_long = input("How long should the manga be? (short, medium, long): ")

                        if short_medium_long.lower() == "short":
                            print("Recommendation: 'I Am a Hero'")
                        else:
                            if short_medium_long.lower() == "medium":
                                print("Recommendation: 'Ajin: Demi-Human'")
                            else:
                                if short_medium_long.lower() == "long":
                                    print("Recommendation: 'Tokyo Ghoul'")


                        else :
                            print("Invalid Input")\n\n''')
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC5()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                
                elif choice == 'r':
                    os.system('cls')
                    break

    elif Choice == 'x':
        print('Thank you For viewing my program')
        break