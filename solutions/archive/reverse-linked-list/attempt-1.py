"""
206. Reverse Linked List  [Easy]  (Linked List)

https://leetcode.com/problems/reverse-linked-list/
Statement: reverse-linked-list.md   ·   Fluency target: 15 min (prior)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head == None:
            return head
        cursor = head
        depth_count = 0
        while cursor.next != None:
            print(cursor.val)
            cursor = cursor.next
            depth_count += 1
        new_head = ListNode(cursor.val, None)
        new_next = new_head
        for i in range(depth_count - 1, -1, -1):
            cursor = head
            for j in range(0, i):
                cursor = cursor.next
            new_next.next = ListNode(cursor.val, next=None)
            new_next = new_next.next
        return new_head
            

TESTS = [
    (([1, 2, 3, 4, 5],), [5, 4, 3, 2, 1]),
    (([1, 2],), [2, 1]),
    (([],), []),
    (([1],), [1]),
    (([1, 2, 3, 4, 5, 6, 7],), [7, 6, 5, 4, 3, 2, 1]),
    (([5, 4, 3, 2, 1, 0],), [0, 1, 2, 3, 4, 5]),
]
