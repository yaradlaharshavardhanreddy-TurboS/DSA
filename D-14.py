#Double linked list delete at beginning

'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes: "))
for i in range(n):
    data=int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Before deletion:")
temp=head
while temp is not None:
    print(temp.data,end="<->")
    temp=temp.next
if head is not None:
    head=head.next
    if head is not None:
        head.prev=None
print("\nAfter deletion:")
temp=head
while temp is not None:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
#delete at begin 
if head is None:
    print("DLL is empty....")
else:
    head=head.next
    if head is not None:
        head.prev=None
print("Doubly Linked list: ")
temp=head
while temp is not None:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")'''

#Doubly linked list delete at end 

'''class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes: "))
for i in range(n):
    data=int(input("Enter value: "))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next is not None:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("Before deletion:")
temp=head
while temp is not None:
    print(temp.data,end="<->")
    temp=temp.next
if head is not None:
    head=head.next
    if head is not None:
        head.prev=None
print("\nAfter deletion:")
temp=head
while temp is not None:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
#delete at end
if head is None:
    print("DLL is empty....")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next is not None:
        print(temp.data,end="<->")
        temp=temp.next
print("tail")'''
