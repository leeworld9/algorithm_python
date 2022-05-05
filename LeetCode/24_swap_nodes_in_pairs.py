from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        # 홀수번째 노드와 짝수번째 노드 주소 스왑
        while cur and cur.next:
            odd, even = cur, cur.next
            odd.next, even.next = even.next, odd
            if prev is not None:
                prev.next = even  # 이전 노드의 방향도 변경된 노드로 수정
            else:
                head = even  # 변경이 이루어졌으면 시작헤더가 2번째 노드로 바뀜
            prev = odd
            cur = prev.next

        return head

