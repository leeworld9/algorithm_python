class MyCircularQueue:
    q_front = None
    q_cursor = None

    class ListNode:
        def __init__(self, val=None, next=None):
            self.val = val
            self.next = next

    def __init__(self, k: int):
        for _ in range(0, k):
            if _ == 0:
                self.q_front = self.ListNode(None)
                cur = self.q_front
            else:
                cur.next = self.ListNode(None)
                cur = cur.next
        cur.next = self.q_front  # 원형 리스트 사용
        self.q_cursor = self.q_front

    def enQueue(self, value: int) -> bool:
        if self.q_cursor.val is not None:
            return False
        else:
            self.q_cursor.val = value
            self.q_cursor = self.q_cursor.next
            return True

    def deQueue(self) -> bool:
        if self.q_front.val is None:
            return False
        else:
            self.q_front.val = None
            self.q_front = self.q_front.next
            return True

    def Front(self) -> int:
        if self.q_front.val is None:
            return -1
        else:
            return self.q_front.val

    def Rear(self) -> int:
        cur = self.q_front
        while cur.next is not self.q_cursor:
            cur = cur.next
        if cur.val is None:
            return -1
        else:
            return cur.val

    def isEmpty(self) -> bool:
        cur = self.q_front
        while cur.next != self.q_front:
            if cur.val is not None:
                return False
            cur = cur.next
        return True

    def isFull(self) -> bool:
        cur = self.q_front
        while cur.next != self.q_front:
            if cur.val is None:
                return False
            cur = cur.next
        return True


myCircularQueue = MyCircularQueue(8)
print(myCircularQueue.enQueue(3))  # return True
print(myCircularQueue.enQueue(9))  # return True
print(myCircularQueue.enQueue(5))  # return True
print(myCircularQueue.enQueue(0))  # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.deQueue())  # return True
print(myCircularQueue.isEmpty())  # return False
print(myCircularQueue.isEmpty())  # return False
print(myCircularQueue.Rear())  # return 0
print(myCircularQueue.Rear())  # return 0
print(myCircularQueue.deQueue())  # return True
