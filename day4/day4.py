def checkIfDecreasing(i):
    current = i % 10
    while i > 0:
        i = i // 10
        if i % 10 > current:
            return True
        current = i % 10
    return False


def checkDoubleDigits(i):
    return i[0] == i[1] or i[1] == i[2] or i[2] == i[3] or i[3] == i[4] or i[4] == i[5]


def checkDoubleDigitsPart2(i):
    return i[0] == i[1] and i[1] != i[2] \
        or i[1] == i[2] and i[1] != i[0] and i[2] != i[3] \
        or i[2] == i[3] and i[2] != i[1] and i[3] != i[4] \
        or i[3] == i[4] and i[3] != i[2] and i[4] != i[5] \
        or i[4] == i[5] and i[4] != i[3]


def main():
    low = 178416
    high = 676461
    count = 0
    countPart2 = 0
    for i in range(low, high):
        if not checkDoubleDigits(str(i)):
            continue
        if checkIfDecreasing(i):
            continue
        count += 1
        if not checkDoubleDigitsPart2(str(i)):
            continue
        countPart2 += 1
    print(f'Part 1: {count} passwords found.')
    print(f'Part 2: {countPart2} passwords found.')

main()