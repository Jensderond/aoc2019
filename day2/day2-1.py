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
data[1] = 12
data[2] = 2

n = 0
while n >= 0:
    data, n = compute(data, n)

print(f'Part 1: {data[0]}')