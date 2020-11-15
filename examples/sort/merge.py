
def merge(left, right):
    l = r = 0

    result = []
    while len(result) < len(left) + len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

        if l == len(left):
            result += right[r:]
        elif r == len(right):
            result += left[l:]

    return result


def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2

    return merge(merge_sort(array[:mid]), merge_sort(array[mid:]))


if __name__ == "__main__":
    #print(merge([1, 3, 5], [2, 4, 5, 6]))

    from random import randint
    MAX = 10
    a = [randint(0, MAX) for _ in range(MAX)]
    print(merge_sort(a))
