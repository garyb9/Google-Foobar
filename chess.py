def solution(src, dest):
    # Your code here

    if src == dest:
        return 0

    visited = []
    for row in range(8):
        rowAp = []
        for col in range(8):
            rowAp.append(0)
        visited.append(rowAp)

    destRow = int(dest / 8)
    destCol = dest % 8
    srcRow = int(src / 8)
    srcCol = src % 8
    visited[srcRow][srcCol] = 1

    step = 0
    sources = [src]
    while True:
        step += 1
        newSources = []
        for new in sources:
            srcRow = int(new / 8)
            srcCol = new % 8

            moves = {
                "moveUpRight": [srcRow - 2, srcCol + 1],
                "moveUpLeft": [srcRow - 2, srcCol - 1],
                "moveLeftUp": [srcRow - 1, srcCol - 2],
                "moveLeftDown": [srcRow + 1, srcCol - 2],
                "moveDownLeft": [srcRow + 2, srcCol - 1],
                "moveDownRight": [srcRow + 2, srcCol + 1],
                "moveRightDown": [srcRow + 1, srcCol + 2],
                "moveRightUp": [srcRow - 1, srcCol + 2]
            }

            for move in moves.keys():
                if (moves[move][0] >= 0) and (moves[move][0] <= 7) and (moves[move][1] >= 0) and (moves[move][1] <= 7):
                    if visited[moves[move][0]][moves[move][1]] == 0:
                        visited[moves[move][0]][moves[move][1]] = step
                        newSources.append(moves[move][0] * 8 + moves[move][1])

        sources = newSources

        if visited[destRow][destCol]:
            return visited[destRow][destCol]

        if step == 6:
            return 6


print("found: ", solution(0, 63))
