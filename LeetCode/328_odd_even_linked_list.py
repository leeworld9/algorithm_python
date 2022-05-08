from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외처리
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while odd.next and even.next:
            # 홀수 노드
            odd.next = odd.next.next
            odd = odd.next
            # 짝수 노드
            even.next = even.next.next
            even = even.next

        # 홀수노드 와 짝수노드 그룹 연결하기
        odd.next = even_head

        return head
