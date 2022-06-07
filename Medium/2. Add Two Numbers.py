class ListNode:
    def __init__(self, val=0, next = None) -> None:
        self.val = val
        self.next = next

def addTwoNumbers(l1:ListNode, l2:ListNode):
    ans = tmp = ListNode()
    carry = 0
    while l1 != None or l2 != None:
        if l1 != None:
            carry += l1.val
            l1 = l1.next
        if l2 != None:
            carry += l2.val
            l2 = l2.next
        tmp.next = ListNode(carry % 10)
        tmp = tmp.next
        carry //= 10
    if carry != 0:
        tmp.next = ListNode(carry)
    return ans.next