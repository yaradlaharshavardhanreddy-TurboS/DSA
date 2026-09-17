# create and print a array

'''
arr = list(map(int, input("Enter the elements : ").split()))
print(arr)
print(*arr) # To unpack the list

'''

#access an element with index values

'''

arr = list(map(int,input("Enter the elements : ").split()))
index = int(input("Enter your index value : "))
print("Element: " , arr[index])

print("Element: " , arr[index]+55)
print(*arr)

'''
# insert , insert at specified index


'''


arr = list(map(int,input("Enter the elements : ").split()))
print(*arr)
index = int(input("Enter your index value : "))
value = int(input("Enter the value to be inserted : "))
arr.insert(index , value)
print(*arr)

arr.append(value)
print(*arr)

'''
# delete , delete at specified index
'''

arr = list(map(int,input("Enter the elements : ").split()))
print(*arr)
value = int(input("Enter the value to be deleted : "))
arr.remove(value)
print(*arr)

index = int(input("Enter your index value : "))
arr.pop(index)
print(*arr)

'''
# search an element and return index value

'''

arr = list(map(int,input("Enter the elements : ").split()))
print(*arr)
value = int(input("Enter the value to be found : "))

found = False

for i in range(len(arr)):
    if arr[i] == value:
        found = True
        print(f"Found at index : {i}" )
        break
    if found == False:
        print("Not in the array")


'''
'''
arr = list(map(int,input("Enter the elements : ").split()))
min = arr[0]
for i in range(1,len(arr)):

    if arr[i] <= min:
        min = arr[i]
print(f"The min element in the array is: {min}")
'''


arr = list(map(int,input("Enter the elements : ").split()))
n = len(arr)
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] >  arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(*arr)





























