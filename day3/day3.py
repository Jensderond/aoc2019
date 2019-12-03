from collections import defaultdict


def read_file():
    with open("input.txt") as f:
        return [line.split(',') for line in f.readlines()]

####################
# Part 1
####################


def calcPositions(wirePaths):
    wires = defaultdict()
    wireNumber = 1
    for path in wirePaths:
        wires[wireNumber] = [(0, 0)]
        for op in path:
            direction = op[0]
            step = int(op[1:])

            if direction == 'R':
                for x in range(step):
                    wires[wireNumber].append(
                        (wires[wireNumber][-1][0] + 1, wires[wireNumber][-1][1]))
            elif direction == 'L':
                for x in range(step):
                    wires[wireNumber].append(
                        (wires[wireNumber][-1][0] - 1, wires[wireNumber][-1][1]))
            elif direction == 'U':
                for x in range(step):
                    wires[wireNumber].append(
                        (wires[wireNumber][-1][0], wires[wireNumber][-1][1] + 1))
            elif direction == 'D':
                for x in range(step):
                    wires[wireNumber].append(
                        (wires[wireNumber][-1][0], wires[wireNumber][-1][1] - 1))

        wireNumber += 1
    return wires


def calcIntersection(positions):
    intersections = []
    for k1, v1 in positions.items():
        for k2, v2 in positions.items():
            if k1 != k2:
                a = set(v1)
                b = set(v2)
                if(a & b):
                    intersections.append(list(a & b))

    s = set()
    for inter in intersections:
        for pos in inter:
            if pos != (0, 0):
                s.add(pos)

    result = []
    for x in list(s):
        result.append(abs(x[0]) + abs(x[1]))
    return result, s

####################
# End Part 1
####################

####################
# Part 2
####################


def calcFewestSteps(wires, intersections):
    intersectionList = list(intersections)
    distances = defaultdict(int)
    for _, v in wires.items():
        counter = 0
        for pos in v:
            if pos in intersectionList:
                distances[str(pos[0]) + str(pos[1])] += counter
            counter += 1
    return distances

####################
# End Part 2
####################


if __name__ == "__main__":
    positions = calcPositions(read_file())
    distance, intersections = calcIntersection(positions)
    fewestSteps = calcFewestSteps(positions, intersections)

    print(f'Part 1: {min(distance)}')
    print(f'Part 2: {min([v for k,v in fewestSteps.items()])}')
