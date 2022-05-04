from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        digit = 0

        # 숫자로 변환 후 합산
        while l1 or l2:
            if l1:
                num += l1.val * (10 ** digit)
                l1 = l1.next
            if l2:
                num += l2.val * (10 ** digit)
                l2 = l2.next
            digit += 1

        # 문자열 변환후 반전
        str_num = [int(x) for x in str(num)][::-1]

        # 리스트 생성
        for i in range(0, len(str_num)):
            if i == 0:
                head = ListNode(int(str_num[i]))
                cur = head
            else:
                cur.next = ListNode(int(str_num[i]))
                cur = cur.next

        return head

