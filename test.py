import string
a = int(input().strip())
printString = string.ascii_lowercase if a==1 else string.ascii_uppercase
print(printString)