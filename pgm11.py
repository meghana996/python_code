def Area_of_triangle(x,y):
    return 0.5*x*y
def Area_of_circle(x):
    return 2*3.14*x
def Area_of_square(x):
    return 2*x
print("select operation")
print("1.Area_of_triangle")
print("2.Area_of_circle")
print("3.Area_of_square")
choice=input("enter choice(1/2/3):")
num1=int(input("enter the firstnumber:"))
num2=int(input("enter the second number:"))
if choice == '1':
    print(0.5,"*",num1,"*",num2,"=",Area_of_triangle(num1,num2))
elif choice == '2':
    print(3.14,"*",num1,"*",num1,"=",Area_of_circle(num1))
elif choice == '3':
    print(num1,"*",num1,"=",Area_of_square(num1))
else:
    print("invalid input")
        