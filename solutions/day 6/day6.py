with open("day6.txt") as file:
    board = []
    for line in file:
        board.append(list(line.rstrip()))

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == "^":
                player = [r, c]
                direction = "up"

    unique = set()
    num_unique = 0
    direction_map = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}

    while True:
        if (player[0], player[1]) not in unique:
            num_unique += 1
            unique.add((player[0], player[1]))

        dr, dc = direction_map[direction]

        if not (0 <= player[0] + dr < len(board)) or not (0 <= player[1] + dc < len(board[0])):
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

    print(num_unique)
