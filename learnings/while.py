# Prints all letters except 'e' and 's'


def printletters(a):
    i = 0
    while i < len(a):
        if a[i] == "e" or a[i] == "s":
            i += 1
            continue
        print("Current Letter :", a[i])
        i += 1


if __name__ == "__main__":
    printletters("arielwinter")
