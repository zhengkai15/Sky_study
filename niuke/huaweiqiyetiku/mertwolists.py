class solution:
    def mergeTwoLists(self,l1,l2):
        
        if l1 == None :
            return l2
        if l2 == None :
            return l1
        if l1.val <= l2.val:
            res = l1
            res.next = mergeTwoLists(l1.next,l2)
        if l1.val >= l2.val:
            res = l2
            res.next = mergeTwoLists(l1,l2.next)
        return res

