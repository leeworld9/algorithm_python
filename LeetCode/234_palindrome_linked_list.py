from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        result = []
        cur = head
        while cur is not None:
            result.append(cur.val)
            cur = cur.next
        if result == result[::-1]:
            return True
        else:
            return False


"""
class LinkedList:
    def __init__(self):
        self.head = None

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, val):
        if self.head is None:  # 첫 값이면 헤더로 설정
            self.head = ListNode(val)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(val)

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


sol = Solution()
linked = LinkedList()
linked.append(1)  # head
linked.append(2)
linked.append(2)
linked.append(1)

# print(linked.print_all())  # 1 2 2 1 None
print(sol.isPalindrome(linked.head))
"""