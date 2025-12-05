import queue

def part1(input):
    ans = 0
    inputs = input.splitlines()

    count = 0
    id_ranges  = []
    for r in inputs:
        if r == '':
            break
        start, end = list(map(int, r.split("-")))
        id_ranges.append((start, end))
        count += 1

    for i in range(count + 1, len(inputs)):
        val = int(inputs[i])
        for start, end in id_ranges:
            if val >=start and val <= end:
                ans += 1
                break

    print(ans)

def part2(input):
    ans = 0
    pq = queue.PriorityQueue()
    inputs = input.splitlines()
    for r in inputs:
        if r == "":
            break
        start, end = list(map(int, r.split("-")))
        pq.put((start, end))

    newpq = queue.PriorityQueue()
    s = 0
    e = 0
    while not pq.empty():
        start, end = pq.get()
        if s == 0:
            s = start
            e = end
        elif start > e:
            newpq.put((s, e))
            s = start
            e = end
        else:
            e = max(end, e)
    newpq.put((s, e))

    while not newpq.empty():
        start, end = newpq.get()
        ans += end - start + 1

    print(ans)


f = open("input.txt")
input = f.read()
part1(input)
part2(input)
