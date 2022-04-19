from typing import Optional
from snippet import LinkedList

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)


"""
sol = Solution()
li = LinkedList()

li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)

#cur = li.head
cur = sol.reverseList(li.head)
while cur is not None:
    print(cur.val)
    cur = cur.next
"""