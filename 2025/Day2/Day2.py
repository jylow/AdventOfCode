
def part1(input):
    ranges = input.split(',')
    ans = 0
    ans2 = 0
    for r in ranges:
        start, end = map(int, list(r.split('-')))
        for i in range(start, end + 1):
            s = str(i)
            l = len(s)

            #part1
            if l % 2 == 0 and s[0:(l // 2)] == s[l // 2:]:
                ans += i

            #part2
            for p in range(1, 16):
                if l % p == 0 and p != l:
                    isValid = True
                    for j in range(1, l // p):
                        if s[0:p] != s[j * p : (j + 1) * p]:
                            isValid = False

                    if isValid:
                        ans2 += i
                        break
    print(ans)
    print(ans2)

f = open("input.txt")
input = f.read()
part1(input)
