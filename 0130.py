class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        h = len(board)
        w = len(board[0])

        def dfs(i, j):
            board[i][j] = 'F'
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xi = x + i
                yj = y + j
                if 0 <= xi < h and 0 <= yj < w and board[xi][yj] == 'O':
                    dfs(xi, yj)

        for j in range(w):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[h-1][j] == 'O':
                dfs(h-1, j)
        for i in range(h):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][w-1] == 'O':
                dfs(i, w-1)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'F':
                    board[i][j] = 'O'
