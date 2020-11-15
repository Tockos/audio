

def bubble(array):
    if len(array) < 2:
        return array

    array = array.copy()

    for last in range(len(array)-1, -1, -1):
        modified = False
        for i in range(last):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                modified = True

        if modified is False:
            return array

    return array


if __name__ == "__main__":
    import functools as ft
    from random import randint
    from timeit import repeat

    MAX = 100
    array = [randint(0, MAX) for _ in range(MAX)]
    best = min(repeat(stmt=ft.partial(bubble, array), number=1000))
    print(f"Best: {best}")

