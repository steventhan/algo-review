import collections

class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        sub_boxes = collections.defaultdict(set)
        empty_cells = []
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub_boxes[i//3*3+j//3].add(board[i][j])
                else:
                    empty_cells.append((i, j))
        self.helper(board, empty_cells, rows, cols, sub_boxes)

    def helper(self, board, empty_cells, rows, cols, sub_boxes):
        if not empty_cells: 
            return True
        i, j = empty_cells[0]
        choices = self.choices(rows[i], cols[j], sub_boxes[i//3*3+j//3])
        for choice in choices:
            board[i][j] = choice
            rows[i].add(choice)
            cols[j].add(choice)
            sub_boxes[i//3*3+j//3].add(board[i][j])
            if self.helper(board, empty_cells[1:], rows, cols, sub_boxes):
                return True
            rows[i].remove(choice)
            cols[j].remove(choice)
            sub_boxes[i//3*3+j//3].remove(board[i][j])
        return False


    def choices(self, row, col, sub_box):
        return [str(i) for i in range(1, 10) if str(i) not in row | col | sub_box]



sudoku = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
sol = Solution()
print(sol.solveSudoku(sudoku))
print(sudoku)
