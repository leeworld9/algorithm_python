from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        node = head
        list = []

        # 리버스 할 값들 리스트에 담아내기
        while node:
            if left <= idx <= right:
                list.append(node.val)
            node = node.next
            idx += 1

        # pop()을 이용하여 역으로 값 담아주기
        idx = 1
        node = head
        while node:
            if left <= idx <= right:
                node.val = list.pop()
            node = node.next
            idx += 1

        return head