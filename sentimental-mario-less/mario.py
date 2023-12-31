# TODO
from cs50 import get_int

height = 0
while True:
    height = get_int("Height : ")
    if height >= 1 and height <= 8:
        break

for row in range(height):
    for space in range(height - row - 1):
        print(" ", end="")

    for column in range(row + 1):
        print("#", end="")
    print()
