def array_diff(a, b):
    l = []
    if not a:
        return []
    if not b:
        return a
    for i in a:
        if i not in b:
            l.append(i)
    return l



print(array_diff([1,2], [1]), [2])
print(array_diff([1,2,2], [1]), [2,2])
print(array_diff([1,2,2], [2]), [1])
print(array_diff([1,2,2], []), [1,2,2])
print(array_diff([], [1,2]), [])
print(array_diff([1,2,3], [1, 2]), [3])