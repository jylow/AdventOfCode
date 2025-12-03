
def part1(input):
    switches = [2, 12]
    banks = input.splitlines()

    for idx, switch in enumerate(switches):
        ans = 0
        for bank in banks:
            arr = []
            last = 0
            for i in range(1, switch):
                biggest = -1
                pos = 0
                for p in range(last, len(bank) - switch + i):
                    x = int(bank[p])
                    if x > biggest:
                        biggest = x
                        pos = p
                arr.append(biggest)
                last = pos + 1
            arr.append(int(max(bank[last:])))
            arr = list(map(str, arr))
            ans += int("".join(arr))

        print(f'Part{idx + 1}: {ans}')

f = open('input.txt')
input = f.read()
part1(input)
