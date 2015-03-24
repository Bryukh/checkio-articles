count = 0


def golden_pyramid(triangle, row=0, column=0, total=0):
    global count
    count += 1
    if row == len(triangle) - 1:
        return total + triangle[row][column]
    return max(golden_pyramid(triangle, row + 1, column, total + triangle[row][column]),
               golden_pyramid(triangle, row + 1, column + 1, total + triangle[row][column]))


def golden_pyramid_d(triangle):
    tr = [row[:] for row in triangle]  # copy
    for i in range(len(tr) - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])
    return tr[0][0]


def count_gold(p):
    global count
    path = 1 << len(p)
    res = 0
    while bin(path).count("1") != len(p) + 1:
        s = ind = 0
        for row in range(len(p)):
            ind += 1 if row > 0 and bin(path)[3:][row] == "1" else 0
            s += p[row][ind]
            count += 1
        res = max(res, s)
        path += 1
    print(count)
    return res

TESTS = [
    [
        [1],
        [2, 1],
        [1, 2, 1],
        [1, 1, 2, 1],
        [1, 1, 1, 2, 1],
        # [1, 1, 1, 2, 2, 9],
        # [1, 1, 1, 2, 2, 9, 1],
    ]
]

print(golden_pyramid(TESTS[0]))
print(golden_pyramid_d(TESTS[0]))
print(count_gold(TESTS[0]))
