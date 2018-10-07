from linked_list import ListNode

def test_linked_list():
    node = ListNode("A")
    node.next = ListNode("B")
    node.next.next = ListNode("C")
    node.next.next.next = ListNode("D")
    node.next.next.next.next = ListNode("E")

    fast = node
    slow = node

    while fast and fast.next:
        temp = []
        slow = slow.next
        fast = fast.next.next

    assert temp == []
    assert slow.val == "C"
