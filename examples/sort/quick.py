
from random import randint

def quick(array):
    if len(array) < 2:
        return array

    pivot = array[randint(0, len(array)-1)]

    low, same, high = [], [], []

    for e in array:
        if e < pivot:
            low.append(e)
        elif e == pivot:
            same.append(e)
        else:
            high.append(e)

    return quick(low) + same + quick(high)


if __name__ == "__main__":
    array = [randint(0, 10) for _ in range(10)]
    print(f"{array} --> {quick(array)}")
