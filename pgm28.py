'''convert string from uppercase to lowercase'''
Str1=input("Enter the string to be converted uppercase: ")

for i in range (0,len(Str1)):

   x=ord(Str1[i])
   if x>=97 and x<=122:
       x=x-32
   y=chr(x)
   print(y,end="")

"""Str1=input("Enter the string to be converted uppercase: ")"""

for i in range (0,len(Str1)):

   x=ord(Str1[i])
   if x<=97 :
       x=x+32
   y=chr(x)
   print(y,end="")
