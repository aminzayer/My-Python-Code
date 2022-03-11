# Given the head of a linked list, rotate the list to the right by k places.


# Example 1:

# Input: head = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Example 2:

# Input: head = [0, 1, 2], k = 4
# Output: [2, 0, 1]
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        tail = head
        n = 1
        while head.next:
            head = head.next
            n += 1
        head.next = tail
        head = head.next

        for i in range(n - k % n - 1):
            head = head.next
        res = head.next
        head.next = None
        return res
