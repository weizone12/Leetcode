class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode):
    ans = tmp = ListNode()
    while list1 and list2:
        if list1.val <= list2.val:
            tmp.next = list1
            list1 = list1.next
        else:
            tmp.next = list2
            list2 = list2.next
        tmp = tmp.next
    if list1:
        tmp.next = list1
    if list2:
        tmp.next = list2
    return ans.next