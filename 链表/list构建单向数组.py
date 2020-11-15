class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


res = [1,2,5,4,6,7,8]
head = ListNode(0)
phead = head
prev = None
for i in res:
    head.val = i
    head.next = ListNode(0)
    prev = head
    head = head.next

prev.next = None
print (phead)