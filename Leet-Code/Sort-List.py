# Given the head of a linked list, return the list after sorting it in ascending order.


# Example 1:

# Input: head = [4, 2, 1, 3]
# Output: [1, 2, 3, 4]

# Example 2:

# Input: head = [-1, 5, 3, 4, 0]
# Output: [-1, 0, 3, 4, 5]

# Example 3:

# Input: head = []
# Output: []
class Solution:
    def merge(self, h1, h2):
        dummy = tail = ListNode()
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        tail.next = h1 or h2
        return dummy.next

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
