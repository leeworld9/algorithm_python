class MyCircularDeque:
    q_front = None
    q_last = None

    class ListNode:
        def __init__(self, val=None, next=None, prev=None):
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, k: int):
        for _ in range(0, k):
            if _ == 0:
                self.q_front = self.ListNode()
                cur = self.q_front
            else:
                cur.next = self.ListNode()
                cur.next.prev = cur
                cur = cur.next
        cur.next = self.q_front
        self.q_front.prev = cur
        self.q_last = self.q_front.prev

    def insertFront(self, value: int) -> bool:
        if self.q_front.val is not None:
            return False
        else:
            self.q_front.val = value
            self.q_front = self.q_front.next
            return True

    def insertLast(self, value: int) -> bool:
        if self.q_last.val is not None:
            return False
        else:
            self.q_last.val = value
            self.q_last = self.q_last.prev
            return True

    def deleteFront(self) -> bool:
        if self.q_front.prev.val is None:
            return False
        else:
            self.q_front.prev.val = None
            self.q_front = self.q_front.prev
            return True

    def deleteLast(self) -> bool:
        if self.q_last.next.val is None:
            return False
        else:
            self.q_last.next.val = None
            self.q_last = self.q_last.next
            return True

    def getFront(self) -> int:
        if self.q_front.prev.val is None:
            return -1
        else:
            return self.q_front.prev.val

    def getRear(self) -> int:
        if self.q_last.next.val is None:
            return -1
        else:
            return self.q_last.next.val

    def isEmpty(self) -> bool:
        cur = self.q_last
        while cur.next != self.q_last:
            if cur.val is not None:
                return False
            else:
                cur = cur.next
        return True

    def isFull(self) -> bool:
        cur = self.q_last
        while cur.next != self.q_last:
            if cur.val is None:
                return False
            else:
                cur = cur.next
        return True


de = MyCircularDeque(3)
print(de.insertLast(1))     # return True
print(de.insertLast(2))     # return True
print(de.insertFront(3))    # return True
print(de.insertFront(1))    # return False
print(de.getRear())         # return 2
print(de.isFull())          # return True
print(de.deleteLast())      # return True
print(de.insertFront(4))    # return True
print(de.getFront())        # return 4
