# TODO
from cs50 import get_float


def get_cents():
    while True:
        changes = get_float("Change Owed: ")
        if changes >= 0:
            break
    cents = changes * 100
    return cents


def calculate_quarters(cents):
    return cents // 25


def calculate_dimes(cents):
    return cents // 10


def calculate_nickels(cents):
    return cents // 5


def calculate_pennies(cents):
    return cents // 1


cents = get_cents()

quarters = calculate_quarters(cents)
cents = cents - quarters * 25

dimes = calculate_dimes(cents)
cents = cents - dimes * 10

nickels = calculate_nickels(cents)
cents = cents - nickels * 5

pennies = calculate_pennies(cents)
cents = cents - pennies * 1

coins = quarters + dimes + nickels + pennies

print(coins)
