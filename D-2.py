#Patterns

#Right angle

'''
n = int(input("Enter the no of rows"))
for i in range(n):
    for j in range(i):
        print("*" , end = " ")
    print()

'''
n = int(input("Enter the no of rows"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 or i==j:
            print("*" , end = " ")
        else:
            print(" ",end= " ")
    print()




'''
#Left Angle

n = int(input("Enter the no of rows"))
for i in range(n):
    for j in range():
        print("*" , end = " ")
    print()
'''







