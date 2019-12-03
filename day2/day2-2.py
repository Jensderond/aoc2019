import numpy as np

def compute(val, pos) -> (list, int):
    if val[pos] == 1:
        val[val[pos + 3]] = val[val[pos + 1]] + val[val[pos + 2]]
        pos += 4
    elif val[pos] == 2:
        val[val[pos + 3]] = val[val[pos + 1]] * val[val[pos + 2]]
        pos += 4
    elif val[pos] == 99:
        pos = -1
    else:
        raise ValueError
    return val, pos

data = list(np.genfromtxt("input.txt", delimiter=",", dtype=int))

for noun in range(0,100):
    for verb in range(0,100):
        position = 0
        val = data.copy()
        val[1], val[2] = noun, verb
        while position >= 0:
            val, position = compute(val, position)
        if val[0] == 19690720:
            print(f'Part 2: {100 * noun + verb}')
            break