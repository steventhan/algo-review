class LinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def __repr__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return "->".join(res)

    def __len__(self):
        return self.length

    def _get(self, index):
        cur = self.head
        while cur and index > 0:
            index -= 1
            cur = cur.next
        return cur, index


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur, index = self._get(index)
        return cur.val if cur and index == 0 else -1


    def add_head(self, val):
        self.add_index(0, val)


    def add_tail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.add_index(len(self), val)


    def add_index(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended 
        to the end of linked list. If index is greater than the length, 
        the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        new = Node(val)
        if index == 0:
            new.next = self.head
            try:
                self.head.prev = new
            except AttributeError:
                self.tail = new
            self.head = new
        elif index == len(self):
            new.prev = self.tail
            try:
                self.tail.next = new
            except AttributeError:
                self.head = new
            self.tail = new
        elif 0 < index < len(self):
            cur, index = self._get(index)
            prev = cur.prev
            cur.prev = new
            prev.next = new
            new.next = cur
            new.prev = prev
        else:
            return
        self.length += 1


    def delete_index(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        node, index = self._get(index)
        if not node: return
        try:
            node.prev.next = node.next
        except AttributeError:
            self.head = node.next

        try:
            node.next.prev = node.prev
        except AttributeError:
            self.tail = node.prev
        self.length -= 1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

    def __repr__(self):
        return str(self.val)
