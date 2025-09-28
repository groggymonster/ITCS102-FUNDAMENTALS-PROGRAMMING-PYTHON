#top part of diamond
print("\t\t *", end="" )
for i in range(1, 11, 1):
    for x in range(10, i, -1):
        print(" ", end=" ")
    for f in range(1, i, 1):
        print("*", end=" ")
    for e in range(1, i, 1):
        print("*", end=" ")
    print()

    # bottom part of diamond
for i in range(1, 11, -1):
    for space in range(10 - i):
        print(" ", end=" ")
    for star in range(2 * i - 1):
        print("*", end=" ")
    print()