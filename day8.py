from collections import defaultdict

board = []
with open("day8.txt") as file:
    for line in file:
        board.append(list(line.rstrip()))
        
        
antennae = defaultdict(list)
for r in range(len(board)):
    for c in range(len(board[0])):
        if board[r][c].isalnum():
            antennae[board[r][c]].append((r,c))

locations = set()
for key in antennae:
    for i in range(len(antennae[key])):
        for j in range(i + 1, len(antennae[key])):
            dr = antennae[key][i][0] - antennae[key][j][0]
            dc = antennae[key][i][1] - antennae[key][j][1]
            a1 = (antennae[key][i][0] + dr, antennae[key][i][1] + dc)
            a2 = (antennae[key][j][0] - dr, antennae[key][j][1] - dc)
            if 0 <= a1[0] < len(board) and 0 <= a1[1] < len(board[0]):
                locations.add(a1)
            if 0 <= a2[0] < len(board) and 0 <= a2[1] < len(board[0]):
                locations.add(a2)
print(len(locations))