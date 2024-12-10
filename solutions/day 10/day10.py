board = []
with open("day10.txt") as file:
    for line in file:
        board.append(list(line.rstrip()))

for row in range(len(board)):
    for col in range(len(board[0])):
        board[row][col] = int(board[row][col])

total_score = 0
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] != 0:
            continue

        summits = set()


        def dfs(row, col, height=0):
            if row < 0 or row >= len(board):
                return 0
            if col < 0 or col >= len(board[0]):
                return 0
            if board[row][col] != height:
                return 0
            if (row, col) in summits:
                return 0
            if height == 9:
                summits.add((row, col))
                return 1
            summits_count = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                summits_count += dfs(row + dr, col + dc, height + 1)
            return summits_count


        current = dfs(row, col)
        total_score += current
print(total_score)
