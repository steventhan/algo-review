class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if self.dfs(i, j, board, 0,  word, set()):
                    return True
        return False

    def dfs(self, i, j, board, char_pos, word, visited):
        # import pdb; pdb.set_trace()
        # print(i, j, char_pos, word)
        if char_pos == len(word) - 1 and board[i][j] == word[char_pos]: return True
        neighbors = self.neighbors(i, j, board)

        if board[i][j] == word[char_pos]:
            visited.add((i, j))
            for neighbor in neighbors:
                if neighbor not in visited:
                    if self.dfs(neighbor[0], neighbor[1], board, char_pos+1, word, visited):
                        return True
            visited.remove((i, j))
        return False

    def neighbors(self, i, j, board):
        num_rows = len(board)
        num_cols = len(board[0])
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        # print([neighbor for neighbor in neighbors if num_rows > neighbor[0] >= 0 and num_cols > neighbor[1] >= 0])
        return [neighbor for neighbor in neighbors if num_rows > neighbor[0] >= 0 and num_cols > neighbor[1] >= 0]

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board3 = [
  ['A','B', 'E'],
  ['S','F', 'E'],
]
board1 = [["a"]]
board2 = [["a", "b"]]
board4 = [
    ["A","B","C","E"],
    ["S","F","E","S"],
    ["A","D","E","E"]
]
sol = Solution()
print(sol.exist(board2, "ba"))
