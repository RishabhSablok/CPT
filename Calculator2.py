def final():
    def basic_calculator():

            print("Welcome to my calculator")
            repeat = True
            # This function adds two numbers

            def add(x, y):
                    return x + y

            # This function subtracts two numbers

            def subtract(x, y):
                   return x - y

            # This function multiplies two numbers

            def multiply(x, y):
                    return x * y

            # This function divides two numbers

            def divide(x, y):
                    return x/y

            # This function squares a number

            def square(x,y):
                    return x**y

            # Take input from the user
            while repeat:
                    print("Select operation.")
                    print("1.Add")
                    print("2.Subtract")
                    print("3.Multiply")
                    print("4.Divide")
                    print("5.Square")
                    choice = int(input("Enter choice(1/2/3/4/5):"))
                    if choice < 6:
                        num1 = eval(input("Enter first number: "))
                        num2 = eval(input("Enter second number: "))

                    if choice == 1:
                        print(num1,"+",num2,"=", add(num1, num2))

                    elif choice == 2:
                        print(num1, "-", num2, "=", subtract(num1 ,num2))

                    elif choice == 3:
                        print(num1,"*",num2,"=", multiply(num1,num2))

                    elif choice == 4:
                           if num2==0:
                                 print("Math Error")
                           else:
                                 print(num1,"/",num2,"=", divide(num1,num2))
                    elif choice==5:
                         print(num1,"^",num2,"=",square(num1,num2))
                    elif choice==0:
                         print("I am so sorry, I cannot process this number please use a number between 1 to 5, Please try again")
                    else:
                          print("I am so sorry, I cannot process this number please use a number between 1 to 5, Please try again")
                    print ("Do you want to calculate again")
                    repeat=("y" or "yes")in input().lower()
            print("Thank you for using my calculator hope to see you again")
            repeat = True

    #######################################################################################################################################################################

    def midpoint():
        repeat=True
        while repeat:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            c=(a+b)/2
            print ("The midpoint of the line is ",c)
            print("Do you want to this again? ")
            repeat=("y" or "yes")in input().lower()

    #######################################################################################################################################################################

    def odd_or_even():
        repeat= True
        while repeat:

            a=int(input("If you give me a number I could tell you if it is odd or even "))
            if a%2==0:
                print("This is an even number")
            else:
                print("This is an odd number")
            print("Do you want to do it again")
            repeat = ("yes" or "y") in input().lower()

    #######################################################################################################################################################################


    def table():
        repeat=True
        while repeat:
            a=0
            b=int(input("Enter which table do you want = "))
            l=int(input("Till what do you want the table to go? "))
            while a<l:
                a=a+1
                c=a*b
                print( b, " X ", a, "=", c)
            print ("Thank you")
            print("Do you want to know another table?")
            repeat=("y" or "yes")in input().lower()

    #######################################################################################################################################################################


    def tax():
        repeat = True
        print("Welcome to my tax calculator")
        while repeat:
            print("The rate in ontario is 13%")
            d=float(input("What percentage is the tax? "))
            a=float(input("What is the amount to be taxed: "))
            b=a*d/100
            c=b+a
            print("The taxable amount is ",a,",the amount of tax payable to government is ",b," and the amount of money payable to the person is ",c)
            print("Do you want to do this again")
            repeat=("y" or "yes")in input().lower()


    #######################################################################################################################################################################


    def mean():
        repeat = True
        kka = True
        counter = 0
        total = 0
        while repeat:
            kka = True
            counter = 0
            total = 0
            while kka:
                a = input("Input the numbers here (Enter a string to stop): ")
                try:
                    a = float(a)
                    total += a
                    counter += 1
                except:
                    kka = False
                    print(total/counter)
                    print("Do you want to do it again?: ", end = "")
                    repeat=("y" or "yes")in input().lower()


    #######################################################################################################################################################################


    def percentage():
        repeat=True
        while repeat:
            print("1. Percentage to decimal")
            print("2. Find the percentage of a number")
            choice=int(input("Input your choice: "))
            if choice==1:
                number=eval(input("Input the percent (Do not use the percent sign)"))
                answer=number/100
                print("The answer is ",answer)
                repeat=("y" or "yes")in input().lower()
            elif choice==2:
                number=eval(input("Input the number "))
                percent=eval(input("Input the percent without the sign "))
                answer=number*percent/100
                print("The answer is",answer)
                repeat=("y" or "yes")in input().lower()

            else :
                print("Invalid Choice")
                repeat=("y" or "yes")in input().lower()


    #######################################################################################################################################################################

    def guess_game():
        from random import randint
        repeat = True
        while repeat:
            b=randint(1,10)
            c=int(input("Guess a number between 1 and 10 "))
            if c == (b):
                print("Right, YOU WON")
            else :
                print("Wrong answer the number is",b)
            print('Do you want to try again')
            repeat = ("y" or "yes" or "Yes" or "Y") in input().lower()


    #######################################################################################################################################################################

    repeat=True
    print("Welcome")
    while repeat:
        print("\tMain Menu\t")
        print("1. Calculator")
        print("2. Midpoint")
        print("3. Odd or Even")
        print("4. Table")
        print("5. Tax")
        print("6. Mean")
        print("7. Percentage")
        print("8. Guess Game")
        user_input=int(input("Print your choice: "))
        if user_input==1:
            basic_calculator()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==2:
            midpoint()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==3:
            odd_or_even()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==4:
            table()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==5:
            tax()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==6:
            mean()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==7:
            percentage()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        elif user_input==8:
            guess_game()
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()
        else:
            print("Invalid Input")
            print("Do you want to go to the main menu?")
            repeat=("y" or "yes") in input().lower()

    else:
        print("Thank you")
final()