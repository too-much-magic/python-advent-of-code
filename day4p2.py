with open("day4.txt", 'r') as file:    
    board = []

    for index1, line in enumerate(file):
        board.append(list(line.rstrip()))

    # board is [ROW][COL]
    def dfs(dr, dc, count=2, r=0, c=0, visited=None):
        if visited is None:
            visited = set()
        if (r, c) in visited or not 0 <= r < len(board) or not 0 <= c < len(board[0]):
            return False

        letters = {"X": 1, "M": 2, "A": 3, "S": 4}

        if letters[board[r][c]] == count:
            visited.add((r, c))
            if count == 4:
                return True
            if dfs(dr, dc, count + 1, r + dr, c + dc):
                return True
            return False


    xmases = 0
    seen = set()
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'M':
                for dr1, dc1 in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
                    if dfs(dr1, dc1, r=row, c=col):
                        directions = {(-1, -1), (1, 1), (-1, 1), (1, -1)}
                        directions.discard((dr1, dc1))
                        directions.discard((-dr1, -dc1))
                        for dr2, dc2 in directions:
                            if dfs(dr2, dc2, r=row + (2 * dr1), c=col) and (
                                    (row, col) not in seen or (row + (2 * dr1), col) not in seen):
                                xmases += 1
                                seen.add((row, col))
                                seen.add((row + (2 * dr1), col))
                                print(row, col, row + (2 * dr1), col)
                            if dfs(dr2, dc2, r=row, c=col + (2 * dc1)) and (
                                    (row, col) not in seen or (row, col + (2 * dc1)) not in seen):
                                xmases += 1
                                seen.add((row, col))
                                seen.add((row, col + (2 * dc1)))

    print(xmases)
