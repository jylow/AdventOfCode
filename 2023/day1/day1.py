
def part1(input):
    input = input.splitlines()

    ans = 0

    for line in input:
        print(line)
        line = [x for x in line if x.isnumeric()]
        #print(line)

        ans += int(line[0]) * 10 + int(line[-1])

    print(ans)

def part2(input):
    spelling = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    input = input.splitlines()

    ans = 0
    for line in input:
        l = []
        for i in range(len(line)):
            if line[i].isnumeric():
                l.append(line[i])
            else:
                for idx, spell in enumerate(spelling):
                    if len(line) - 1 - len(spell) >= 0 and spell == line[i: i + len(spell)]:
                        l.append(str(idx+ 1))


        ans += int(l[0]) * 10 + int(l[-1])

    print(ans)

f = open("day1.in")
input = f.read()
print("PART1")
#part1(input)
print("PART2")
part2(input)

