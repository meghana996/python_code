'''convert string to lowercase'''
Str1=input("Enter the string to be converted lowercase: ")

for i in range (0,len(Str1)):

   x=ord(Str1[i])
   if x<=97: 
       x=x+32
   y=chr(x)
   print(y,end="")

