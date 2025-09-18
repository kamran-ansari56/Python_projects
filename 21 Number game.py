def nearestMultiple(num):
    if num >=4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose1():
    print("\n\nYou Lose")
    print("Bettter Luck Next Time")
    exit()

def check(xyz):
    i = 1
    while i < len(xyz):
        if (xyz[i] - xyz[i-1] != 1):
            return False
        i = i+1
    return True