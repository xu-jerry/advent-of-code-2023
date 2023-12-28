with open('input.txt') as f:
    lines = f.readlines()
    time = [int(num) for num in lines[0].split(":")[1].split()]
    distance = [int(num) for num in lines[1].split(":")[1].split()]

    res = 1

    for i, t in enumerate(time):
        total = 0
        beg = 0
        for j in range(t):
            if (t-j)*j > distance[i]:
                beg = j
                break
        total = t - 2 * beg + 1
        res *= total
        print(total)
    print(res)