
def part1(input):

    red = 12
    green = 13
    blue = 14
    ans = 0


    for line in input:
        cond = True
        game, info = line.split(':')
        _ , id = game.strip().split(' ')
        id = int(id)

        tries = info.strip().split(';')

        for t in tries:
            pull = t.split(',')
            for p in pull:
                val, color = p.strip().split(' ')

                val = int(val.strip())
                match color.strip():
                    case 'red':
                        cond &= (val <= red)
                    case 'green':
                        cond &= (val <= green)
                    case 'blue':
                        cond &= (val <= blue)

        if cond:
            ans += id

    print(ans)
    return

def part2(input):
    ans = 0

    for line in input:
        red = 0
        green = 0
        blue = 0
        game, info = line.split(':')
        _ , id = game.strip().split(' ')
        id = int(id)

        tries = info.strip().split(';')

        for t in tries:
            pull = t.split(',')
            for p in pull:
                val, color = p.strip().split(' ')

                val = int(val.strip())
                match color.strip():
                    case 'red':
                        red = max(red, val)
                    case 'green':
                        green = max(green, val)
                    case 'blue':
                        blue = max(blue, val)


        ans += red * green * blue
    print(ans)
    return

f = open('day2.in')
input = f.readlines()

print("PART1")
part1(input)
print("PART2")
part2(input)

