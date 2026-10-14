# LIFO
# Stack Operations - Push


'''
stack = []
n = int(input("Enter number of elements : "))
for i in range(n):
    value = int(input("Enter the value:"))
    stack.append(value)
print(f"Stack {stack}")
'''
# Stack Operations - push / peek / pop

'''

stack = []
n = int(input("Enter number of elements : "))
for i in range(n):
    value = int(input("Enter the value:"))
    stack.append(value)
print("Stack ",stack)
print("Stack peek element: " ,{stack[-1]})
print("Removed Element: ",stack.pop())
print("Stack ", stack)
print("Stack peek element: ", stack[-1])

'''

# Stack Operations - Stack isEmpty

'''

stack=[]
n = int(input("Enter the no of elements: "))
for i in range(n):
    value = int(input("Enter the value :"))
    stack.append(value)
print("Stack", stack)
while len(stack)>0:
    print("Popped Value:", stack.pop())

if len(stack)==0:
    print("Stack is Empty")


'''




# Stack OPerations - Overflow Condition

'''

stack=[]
size = int(input("Enter the size of the stack"))
n = int(input("Enter the no of elements: "))
for i in range(n):
    value = int(input("Enter the value :"))
    if len(stack)<size:
        stack.append(value)
    else:
        print("Stack Overflow")
print("Stack",stack)

'''

# Stack Operations - Merge two sets

'''

stack1 = []
stack2 = []
merged = []
n1 = int(input("Enter number of elements : "))
for i in range(n1):
    value = int(input("Enter the value:"))
    stack1.append(value)

n2 = int(input("Enter number of elements : "))
for i in range(n2):
    value = int(input("Enter the value:"))
    stack2.append(value)

i,j = 0,0

while i<len(stack1) and j<len(stack2):
    if stack1[i]<stack2[j]:
        merged.append(stack1[i])
        i+=1

    else:
        merged.append(stack2[j])
        j+=1

while i<len(stack1):
    merged.append(stack1[i])
    i+=1


while j<len(stack2):
    merged.append(stack2[j])
    j+=1

print(merged)

'''