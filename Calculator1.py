print("Welcome to my calculator")
repeat= True
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
def exponent(x,y):
         return x**y
# Take input from the user
while repeat:
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Exponent")
        choice = int(input("Enter choice(1/2/3/4/5):"))
        if 0 < choice < 6:
              num1 = eval(input("Enter first number: "))
              num2 = eval(input("Enter second number: "))

        if choice == 1:
            print(num1,"+",num2,"=", add(num1,num2))

        elif choice == 2:
            print(num1,"-",num2,"=", subtract(num1,num2))

        elif choice == 3:
            print(num1,"*",num2,"=", multiply(num1,num2))

        elif choice == 4:
               if num2==0:
                     print("Math Error")
               else:
                     print(num1,"/",num2,"=", divide(num1,num2))
        elif choice==5:
             print(num1,"^",num2,"=",exponent(num1,num2))
        else:
              print("I am so sorry, I cannot process this number please use a number between 1 to 5, Please try again")
        print ("Do you want to calculate again")
        repeat=("y" or "yes" or "Yes" or "Y" or "YES")in input().lower()
print("Thank you for using my calculator hope to see you again")
