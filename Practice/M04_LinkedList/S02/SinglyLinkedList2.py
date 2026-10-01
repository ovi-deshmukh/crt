'''
Singly Linked List :
Algorithm:
1. Create Node
2. Insert the data into the nodes
3. Generate the connection btw the nodes
4. Traverse all the nodes


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node1.next = node2
node2.next = node3
node3.next = node4
def traverse():
    curr = node1
    while curr:
        print(curr.data,end = " -> " )
        curr = curr.next
    print("None")
traverse()
'''
# Operations:
# 1. Insertion: 3 ways 
        # a) Insertion at the beginning
        # b) Insertion at the end
        # c) Insertion at the specified node
# 2. Deletion
# 3. Traverse
# 4. Update

# a) Insertion at the beginning in singly linked list:
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def deletion_begin(head):
    if head is None:
        print("Error")
        return None
    new_head = head.next
    del  head
    return new_head

def insert_end(head,data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    return head 

def deletion_end(head):
    if head is None or head.next is None:
        print("Error")
        return None
    curr = head
    while curr.next.next:
        curr = curr.next
    del_node = curr.next
    curr.next = None
    del del_node
    return head

def insert_at_pos(node,data):
    if node is None:
        print("Error")
        return 
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node

def deletion_at_pos(node):
    if node is None or node.next is None:
        print("Error")
        return
    next_node = node.next
    node.next = next_node.next
    del next_node

def traverse(head):
    curr = head
    while curr:
        print(curr.data,end = " -> " )
        curr = curr.next
    print("None")

head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
head = insert_begin(head, 40)

print("Insertion at the begin")
traverse(head)
print()

print("Insertion at the End")
insert_end(head, 400)
traverse(head)
print()

print("Insertion at the Position")
insert_at_pos(head, 100)
traverse(head)
print()

print("Deletion at the Beginning")
head = deletion_begin(head)
traverse(head)
print()

print("Deletion at the End")
head = deletion_end(head)
traverse(head)
print()

print("Deletion at the Position")
deletion_at_pos(head.next)
traverse(head)
print()
'''
Deletion: 3 Ways
    a) Deletion at the beginning
    b) Deletion at the end
    c) Deletion at the specified node
'''