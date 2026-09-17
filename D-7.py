# count the occurences in a array
'''
a = input("Enter fruits : ").split()
key = input("Enter  a fruit: ")
count = 0
for i in range(len(a)):
    if a[i] == key:
        count+=1
print(count)

'''

'''
a = input("Enter fruits : ").split()
for i in range(len(a)):
    count = 0
    for j in range(1,len(a)):
        if a[i] == key:
            count+=1

    print(count)
'''

# write a code to reverse a string

'''

s = input("Enter the string: ")
s1 = ""
for i in s:
    s1=i+s1
print(f"The reversed string is {s1}")

'''
# count the occurences of letters in a word

'''
s = input("Enter the string: ") 
for i in s:
    c=0
    for j in s:
        if j==i:
            c+=1
    print(f"charchter ' {i} ' is repeated {c} in the given string")
        

'''
# Largest string in a L ist

'''

l = input().split()
largest = len(l[0])
for i in l:
    if len(i) > largest:
        largest = len(i)
        print(f"the largest animal is {i} with length of {largest}")
        break

'''














