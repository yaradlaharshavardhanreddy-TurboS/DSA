 # math approach
# Area , cir
'''

n = int(input("Enter the value of n: "))
area = 3.14159 * n * n
cir = 2* 3.14159 * n
print("Area: " , area)
print("Circumference: " , cir)

'''


# math approach series expression
# Factorial
'''

import math
n = int(input("Enter the number: "))
s = 0
for i in range(1,n+1):
    s+=math.factorial(i)/(i+1)
print(s)

'''

# Factorial

'''
n = int(input("Enter a number: "))
s = 0
f = 1
for i in range(1,n+1):
    f = f*i
    s+= f/(i+1)
print(s)

'''

# Naive Approach
# Max in a List

'''

l = list(map(int,input("Enter the numbers in the list ").split()))
max = l[0]
for i in range(1,len(l)):
    if l[i] > max:
        max = l[i]
print(f"max number in the given list : {max}")

'''

# Brute Force
# Anagram Tom Riddles
str1 = input("Enter a string1").lower().replace(" ","")
str2 = input("Enter a string2").lower().replace(" ","")

str1 = sorted(str1)
str2 = sorted(str2)

if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print(f"{str1} is Anagram with {str2}")
else:
    print(f"{str1} is Not a Anagram with {str2}")















