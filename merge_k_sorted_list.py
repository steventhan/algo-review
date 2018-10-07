from node import Node


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        print(lists)
        buffer = []
        for lst in lists:
            cur = lst
            while cur:
                nxt = cur.next
                buffer.append(cur)
                cur.next = None
                cur = nxt
        buffer.sort(key=lambda x: x.val)
        for i in range(len(buffer)-1):
            buffer[i].next = buffer[i+1]

        return buffer[0] if buffer else []

node1a = Node(1)
node1b = Node(1)
node2 = Node(2)
node3 = Node(3)
node4a = Node(4)
node4b = Node(4)
node5 = Node(5)
node6 = Node(6)

node1a.next = node4a
node4a.next = node5

node1b.next = node3
node3.next = node4b

node2.next = node6
k = [
    node1a, node1b, node2
]
sol = Solution()
print(sol.mergeKLists(k))
