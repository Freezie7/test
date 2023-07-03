def movement (m):
    true_or_false = False
    ud = 0
    rl = 0
    for i in m:
        if i == "U":
            ud += 1
        elif i == "D":
            ud -= 1
        elif i == "R":
            rl += 1
        elif i == "L":
            rl -= 1
    if ud == 0 and rl == 0:
        true_or_false = True
    return (true_or_false)

def movement2 (m):
    true_or_false = False
    udrl = 0
    lists = list(m)
    j = len(lists)
    dicts = {
        "U":1, "D": -1, "R":1, "L":-1
    }
    for i in m:
        udrl += dicts[lists[len(lists) - j]]
        j -= 1
    if udrl == 0:
        true_or_false = True
    return true_or_false



move = input("вверх(‘U’), вниз(‘D’), вправо(‘R’) и влево(‘L’): ")
print(movement2(move))
