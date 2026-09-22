# Find a square root of a number using binary search evaluation

'''
n=int(input("enter a number:"))
low=0
high=n
ans=0
while low<=high:
    mid=(low+high)//2
    if mid*mid<=n:
        ans=mid
        low=mid+1
    else:
        high=mid-1
        print("square root",ans)


'''

# Find the First occurence of a number in a array

'''

arr = list(map(int,input("Enter the elements: ").split()))
target = int(input("EBter a number: "))
low = 0
high = len(arr) - 1
ans = -1
while low <= high:
    mid = (low+high)//2
    if arr[mid] == target:
        ans = mid
        high = mid - 1
    elif arr[mid]<target:
        low = mid+1
    else:
        high = mid - 1

print("First Occurence" ,ans)

'''


# Find the Last occurence of a number in a array


arr = list(map(int,input("Enter the elements: ").split()))
target = int(input("EBter a number: "))
low = 0
high = len(arr) - 1
ans = -1
while low <= high:
    mid = (low+high)//2
    if arr[mid] == target:
        ans = mid
        low = mid + 1
    elif arr[mid]<target:
        low = mid+1
    else:
        high = mid - 1

print("Last Occurence" ,ans)

 

