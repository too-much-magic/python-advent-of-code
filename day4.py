with open("day4.txt", 'r') as file:
    board = []
    
    for index1,line in enumerate(file):
        board.append(list(line.rstrip()))
    
    # board is [ROW][COL]
    
    def dfs(dr, dc, count = 1, r=0, c=0, visited=None):
        if visited is None:
            visited = set()
        if (r, c) in visited or not 0 <= r < len(board) or not 0 <= c < len(board[0]):
            return False
        
        letters = {"X":1, "M":2, "A":3, "S":4}

        if letters[board[r][c]] == count:
            visited.add((r, c))
            if count == 4:
                return True
            if dfs(dr, dc, count+1,r+dr,c+dc):
                return True
            return False
            
    xmases = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'X':
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                    if dfs(dr, dc, r=row, c=col):
                        xmases += 1
    
    print(xmases)