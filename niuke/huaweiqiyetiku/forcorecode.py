class ListNode:
    def __init__(self,x):
        self.next = None
        self.val = x
class Solution:
    def ReverseList(self,pHead):


if __name__ == '__main__':
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    s= Solution()
    tmp =s.ReverseList(head)
    while tmp:
        print(tmp.val)
        tmp =tmp.next
