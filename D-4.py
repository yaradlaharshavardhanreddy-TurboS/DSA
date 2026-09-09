# Types of recursion
# Direct Recursion

'''
def numbers(n):
    if n==0:
        print("Done")
        return
    print(n, end = ' ')
    numbers(n-1)
n = int(input("Enter a value"))
numbers(n)

'''

# In-Direct Recursion


'''
def even(n):
    if n==0:
        print(copy , "is Even")
        return 
    odd(n-1)
def odd(n):
    if n==0:
        print(copy  , "is Odd")
        return
    even(n-1)

n = int(input("Enter a value"))
copy = n
even(n)

'''

# Tree Recursion

'''
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
n = int(input("Enter the Value"))
for i in range(n):
    print(fib(i), end = ' ')

'''

'''
def tree(n):
    if n<=0:
        return
    print(n, end = ' ')
    tree(n-1)
n = int(input("Enter a number : "))
tree(n)
'''

# Head Recursion

def head(n):
    if n==0:
        return 
    head(n-1)
    print(n)

n = int(input("Enter a value : "))
head(n)
