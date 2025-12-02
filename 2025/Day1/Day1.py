

def part1(input):
    ans = 0
    ans2 = 0
    curr = 50
    for val in input:
        dir = val[0]
        num = int(val[1:])
        print(ans2)
        print("___")
        if dir == 'L':
            old = curr
            curr = (curr - num) % 100
            passes = ((100 - old) % 100 + num) // 100
            ans2 += passes
        else:
            old = curr
            curr = (old + num) % 100
            passes = (old + num) // 100
            ans2 += passes
        if curr == 0:
            ans+=1

    print(f'Part1: {ans}')
    print(f'Part2: {ans2}')



f = open("input.txt")
input = f.read().splitlines()
part1(input)
