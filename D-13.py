# SLL insert at end

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
tail = None

values = list(map(int, input("Enter values: ").split()))

for value in values:
    newnode = Node(value)
    if head is None:
        head = newnode
        tail = newnode
    else:
        tail.next = newnode
        tail = newnode

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("Tail")

'''

# SLL Inserting at beginning

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
tail = None

values = list(map(int, input("Enter values: ").split()))


for value in values:
    newnode = Node(value)
    newnode.next = head
    head = newnode

current = head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next

print("Tail")

'''




