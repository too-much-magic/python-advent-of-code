board = []
with open("day10.txt") as file:
    for line in file:
        board.append(list(line.rstrip()))

for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] == '.':
            board[row][col] = -2
        else:
            board[row][col] = int(board[row][col])

total_ratings = 0
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != 0:
            continue

        paths = set()


        def dfs(row, col, height=0, path=None):
            if path is None:
                path = [(row, col)]
            if row < 0 or row >= len(board):
                return 0
            if col < 0 or col >= len(board[0]):
                return 0
            if board[row][col] != height:
                return 0
            if height == 9:
                if tuple(path) in paths:
                    return 0
                paths.add(tuple(path))
                return 1
            paths_count = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_path = path.copy()
                new_path.append((row + dr, row + dc))
                paths_count += dfs(row + dr, col + dc, height + 1, new_path)
            return paths_count
        
        current = dfs(row, col)
        total_ratings += current
print(total_ratings)