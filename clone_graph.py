from collections import deque
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return "id: {} | label: {} | neighbors {}".format(id(self), self.label, len(self.neighbors))

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        clone = UndirectedGraphNode(node.label)
        queue = deque()
        clone_queue = deque()
        queue.append(node)
        clone_queue.append(clone)
        visited = set()
        clones = {clone.label: clone}

        while queue:
            print("Current queue {} -> {}".format(queue, len(queue)))
            current = queue.popleft()
            print("Clone queue {} -> {}".format(clone_queue, len(clone_queue)))
            current_clone = clone_queue.popleft()
            if current in visited:
                continue
            visited.add(current)
            for neighbor in current.neighbors:
                # import pdb; pdb.set_trace()
                if neighbor.label in clones:
                    neighbor_clone = clones[neighbor.label]
                else:
                    neighbor_clone = UndirectedGraphNode(neighbor.label)
                    clones[neighbor.label] = neighbor_clone
                current_clone.neighbors.append(neighbor_clone)
                clone_queue.append(neighbor_clone)
                queue.append(neighbor)
        return clone



sol = Solution()
node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
# node2 = UndirectedGraphNode(2)
node0.neighbors = [node1]
node1.neighbors = [node0]
# node2.neighbors = [node2]
print(node0)
clone = sol.cloneGraph(node0)
print(clone.neighbors[0].neighbors)
print(clone)
