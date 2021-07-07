class ListNode:
    def __init__(self,x):
        self.next = None
        self.val = x

if __name__ == '__main__':
    data = [5, 1, 7, 96]
    tail = head = ListNode(data[0])
    for x in data[1:]:
        print(tail.val)
        tail.next = ListNode(x) # Create and add another node
        tail = tail.next # Move the tail pointer
