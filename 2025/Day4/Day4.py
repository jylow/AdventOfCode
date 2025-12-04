

def part1(input):
    input = input.splitlines()
    ans = 0
    rows = len(input)
    cols = len(input[0])
    debug = [['.'for i in range(cols)] for j in range(rows)]
    for row in range(rows):
        for col in range(cols):
            #guard
            if input[row][col] != '@':
                continue
            papers = 0
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if c == 0 and r == 0:
                        continue
                    if check_bounds(row + r, col + c, rows, cols) and input[row + r][col + c] == '@':
                        papers+=1
            if papers < 4:
                ans += 1
                debug[row][col] = 'x'

    #print(debug)
    print(f"Part1: {ans}")


def part2(input):
    input = input.splitlines()
    input = list(map(list, input))
    ans = 0
    rows = len(input)
    cols = len(input[0])
    count = 1
    while count != 0:
        count = 0
        for row in range(rows):
            for col in range(cols):
                #guard
                if input[row][col] != '@':
                    continue
                papers = 0
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        if c == 0 and r == 0:
                            continue
                        if check_bounds(row + r, col + c, rows, cols) and input[row + r][col + c] == '@':
                            papers+=1
                if papers < 4:
                    ans += 1
                    input[row][col] = "."
                    count += 1

    print(f"Part2: {ans}")

def check_bounds(row, col, right, down):
    if row < 0 or col < 0:
        return False
    if row >= right or col >= down:
        return False
    return True

f = open("input.txt")
input = f.read()
part1(input)
part2(input)
