# Generating numbers n times

'''
n = int(input("Enter a number : "))
for i in range(n):
    print('India')

'''


#Generating numbers n times ans finding its sum
'''
n = int(input("Enter a number : "))
sum = 0
for i in range(n):
    print(i , end = ' ')
    sum+=i
print()
print(f"Sum is {sum}")

'''
# math approach series expression

'''
import math
n = int(input("Enter the number: "))
s = 0
for i in range(1,n+1):
    s+=math.factorial(i)/i+1
print(s)

'''










