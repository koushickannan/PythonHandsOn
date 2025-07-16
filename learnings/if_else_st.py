
if __name__ == '__main__':

    n = int(input().strip())
    if n % 2 == 1:
        print("Wierd")
    elif n % 2 == 0 and n in range(2, 5):
        print("Not Wierd")
    elif n % 2 == 0 and n in range(6, 20):
        print("Wierd")
    elif n % 2 == 0 and n > 20:
        print("Not Wierd")
