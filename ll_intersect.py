from node import Node
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return
        len_a = 0
        len_b = 0
        cur_a = headA
        cur_b = headB
        while cur_a or cur_b:
            if cur_a:
                len_a += 1
                cur_a = cur_a.next
            if cur_b:
                len_b += 1
                cur_b = cur_b.next

        print(len_a, len_b)

        if len_a < len_b:
            shorter = headA
            longer = headB
        else:
            shorter = headB
            longer = headA
        shortened_longer = self.move_head(shorter, longer, abs(len_a - len_b))
        print(shorter, shortened_longer)

        while shorter and shortened_longer:
            if shorter is shortened_longer: return shorter
            shorter = shorter.next
            shortened_longer = shortened_longer.next

    def move_head(self, shorter, longer, length_diff):
        i = 0
        while i < length_diff:
            longer = longer.next
            i += 1
        return longer

sol = Solution()
node1 = Node(1)
print(sol.getIntersectionNode(node1, node1))
