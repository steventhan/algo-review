from node import Node

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = second = head
        for i in range(n):
            first = first.next

        prev = None
        while first:
            prev = second
            first = first.next
            second = second.next
        if prev:
            prev.next = second.next
            return head
        return None

sol = Solution()
node1 = Node(1)
node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

sol.removeNthFromEnd(node1, 2)
cur = node1
while cur:
    print(cur)
    cur = cur.next
