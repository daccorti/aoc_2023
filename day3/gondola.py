import math, re
from string import digits

board = list(open("part_a.txt"))
dims = len(board)

vals = {
    (r, c): []
    for r in range(dims)
    for c in range(dims)
    if board[r][c] not in digits and board[r][c] not in "."
}

for r, row in enumerate(board):
    for n in re.finditer(r"\d+", row):
        edge = {(r, c) for r in (r - 1, r, r + 1) for c in range(n.start() - 1, n.end() + 1)}

        for o in edge & vals.keys():
            vals[o].append(int(n.group()))

print(f"part 1:{sum(sum(p) for p in vals.values())}")
print(f"part 2: {sum(math.prod(p) for p in vals.values() if len(p)==2)}")
