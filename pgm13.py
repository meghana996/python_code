def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y

print("select operation")
print("1.add")
print("2.subtract")
print("3.multiplication")
print("4.division")

choice=input("enter the choice(1/2/3/4):")
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

if choice=='1':
    print(num1, "+", num2, "=", add(num1,num2))
    
elif choice=='2':
    print(num1, "-", num2, "=", subtract(num1,num2))
    
elif choice=='3':
    print(num1, "*", num2, "=", multiplication(num1,num2))
    
elif choice=='4':
    print(num1, "/", num2, "=", division(num1,num2))
    
else:
    print("invalid input")