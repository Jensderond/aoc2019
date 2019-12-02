import numpy as np

def run(val, n):
    if val[n] == 1:
        val[val[n + 3]] = val[val[n + 1]] + val[val[n + 2]]
        n += 4
    elif val[n] == 2:
        val[val[n + 3]] = val[val[n + 1]] * val[val[n + 2]]
        n += 4
    elif val[n] == 99:
        n = -1
    else:
        raise(Exception("Unknown opcode"))
    return val, n

val = np.genfromtxt("input.txt", delimiter=",", dtype=int)
val[1] = 12
val[2] = 2

n = 0
while n >= 0:
    val, n = run(val, n)

print(val[0])