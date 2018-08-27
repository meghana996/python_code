'''concatenate two strings'''

print("enter 'x' for exit");
string1 = input("enter first string to concatenate:");

if string1 == 'x':
    exit();
    
else:
    string2 = input("enter second string to concatenate:");
    string3 = string1 + string2;
    print("string after concatenation=", string3);
   