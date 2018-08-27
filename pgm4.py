'''program to check the count of vowels in a given string'''

string = input("enter string:")
vowels = 0

for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
        
print("number of vowels are:")
print(vowels)