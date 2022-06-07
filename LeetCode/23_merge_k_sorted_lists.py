from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for li in lists:
            while li:
                array.append(li.val)
                li = li.next

        array.sort()
        head = None
        for i in array:
            if head is None:
                head = ListNode(i)
                cur = head
            else:
                cur.next = ListNode(i)
                cur = cur.next

        return head


arr = []
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
arr.append(l1)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
arr.append(l2)
l3 = ListNode(2)
l3.next = ListNode(6)
arr.append(l3)

sol = Solution()
sol.mergeKLists(arr)

print("end")
