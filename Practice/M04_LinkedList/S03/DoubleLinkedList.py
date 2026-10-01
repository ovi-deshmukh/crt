'''
Double Linked List :
Data store Nodes
Nodes 3 parts
1. data
2. prev
3. next

Algorithm :
1. Create Nodes
2. Insert data
3. Connection btw nodes
4. Traverse

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

def traverse_forward():
    curr = node1
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")

def traverse_backward():
    curr = node4
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.prev
    print("None")
traverse_forward()
traverse_backward()
'''

#Insertion at the beginning:

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node

def deletion_begin(head):
    if head is None:
        print("Error: List is empty")
        return None
    new_head = head.next
    if new_head:
        new_head.prev = None    
    del head   
    return new_head

def insert_after_pos(node,data):
    if node is None:
        print("Error")
        return None
    new_node = Node(data)
    new_node.next = node.next
    new_node.prev = node
    if node.next:
        node.next.prev = new_node
    node.next = new_node

def insert_before_pos(node, data):
    if node is None:
        print("Error")
        return head
    new_node = Node(data)
    new_node.prev = node.prev
    new_node.next = node
    if node.prev:
        node.prev.next = new_node
    else:
        head = new_node
    node.prev = new_node
    return head

def insert_end(head, data):
    new_node = Node(data)
    if head == None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr
    return head



def traverse(head):
    curr  =head
    while curr :
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")

head = None
head = insert_begin(head, 10)
head = insert_begin(head, 30)
head = insert_begin(head, 50)

print("Insertion at the begin")
traverse(head)
print()


print("Insertion at the End")
head = insert_end(head, 100)
traverse(head)
print()

print("Insertion after the Pos")
insert_after_pos(head, 100)
traverse(head)
print()

print("Insertion Before the Pos")
head = insert_before_pos(head, 55)
traverse(head)
print()

print("Deletion  at the Beginning")
head = deletion_begin(head)
traverse(head)
print()