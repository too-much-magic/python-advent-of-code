with open("day6.txt") as file:
    board = []
    for line in file:
        board.append(list(line.rstrip()))
    
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "^":
                player = [r,c]
                direction = "up"
                
direction_map = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
num_loops = 0
initial = (player[0],player[1])

for row in range(len(board)):
    for col in range(len(board[0])):
        player[0],player[1] = initial
        direction = "up"
        if [row,col] == player or board[row][col] == "#":
            continue
        else:
            board[row][col] = "#"
            unique = set()
            while True:
                if (player[0], player[1], direction) in unique:
                    inf_loop = True
                    break
                else:
                    unique.add((player[0],player[1], direction))

                dr,dc = direction_map[direction]
                
                if not (0 <= player[0] + dr < len(board)) or not (0 <= player[1] + dc < len(board[0])):
                    inf_loop = False
                    break
        
                if board[player[0] + dr][player[1] + dc] == "#":
                    if direction == "up":
                        direction = "right"
                    elif direction == "right":
                        direction = "down"
                    elif direction == "down":
                        direction = "left"
                    elif direction == "left":
                        direction = "up"
                        
                else:
                    player[0] += dr
                    player[1] += dc
            
            if inf_loop:
                num_loops += 1
            board[row][col] = "."
print(num_loops)