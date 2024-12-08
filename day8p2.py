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
            
            fwd = bwd = (antennae[key][i][0], antennae[key][i][1])
            
            while 0 <= fwd[0] < len(board) and 0 <= fwd[1] < len(board[0]):
                locations.add(fwd)
                fwd = (fwd[0] + dr, fwd[1] + dc)
            
            while 0 <= bwd[0] < len(board) and 0 <= bwd[1] < len(board[0]):
                locations.add(bwd)
                bwd = (bwd[0] - dr, bwd[1] - dc)

print(len(locations))