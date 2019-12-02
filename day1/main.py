import os
import math
with open("./input.txt") as f:
        content = f.readlines()
content = [x.strip() for x in content]

def calcMass(moduleMass: int) -> int:
    return math.floor(moduleMass / 3) - 2

def calcFuel(moduleFuel: int) -> int:
    fuelTotal = 0
    while True:
        if moduleFuel <= 0: break
        moduleFuel = calcMass(moduleFuel)
        if moduleFuel > 0: fuelTotal += moduleFuel
    return fuelTotal

def main():
    sumOfFuel = 0
    sumOfFuelExtra = 0
    for x in content:
        fuelMass = calcMass(int(x))
        fuel = calcFuel(fuelMass)
        sumOfFuel += fuelMass
        sumOfFuelExtra += fuelMass + fuel

    print(f'Sum of total fuel by mass: {sumOfFuel}')
    print(f'Sum of total fuel by mass and the mass of the fuel: {sumOfFuelExtra}')

main()