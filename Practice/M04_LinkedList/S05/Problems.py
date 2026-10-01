#876. Middle of the Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Solution - 1
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid_ind = count // 2
        temp = head
        for i in range(mid_ind):
            temp = temp.next

        return temp

#Solution - 2(using fast and slow pointer approach)
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow 
    
# 141. Linked List Cycle
# Solution - 1
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        temp = head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False

#Solution - 2(using fast and slow pointer approach)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    
# 19. Remove Nth Node From End of List
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        dummy = ListNode()
        dummy.next = head

        temp = dummy
        for i in range(count - n):
            temp = temp.next
        
        temp.next = temp.next.next

        return dummy.next
    
# 21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        new_node = ListNode()
        temp = new_node
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return new_node.next

# 206. Reverse Linked List
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)

        head.next.next = head
        head.next = None

        return new_head