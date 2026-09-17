# Bubble Sort

'''

a = list(map(int,input("Enter the numbers ").split()))
n = len(a)
for i in range(n):
    for j in range(0 , n-i-1):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
print(f"Sorted Array: {a}")

'''

# Selection Sort

arr = list(map(int,input("ENter the elements :").split()))
for i in range(len(arr)):
    min_index = i
    for j in range(i+1 , len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i] , arr[min_index] = arr[min_index] , arr[i]
    print(arr)

# Insertion Sort

