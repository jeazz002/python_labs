# 1
array1 = [3, -1, 5, 5, 0]
array2 = [42]
array3 = [-5, -2, -9]
array4 = [1.5, 2, 2.0, -3.1]
array5 = []


def min_max(nums: list[float | int]):
    n = [a for a in nums]
    if len(n) != 0:
        return min(n), max(n)
    if len(n) == 0:
        raise ValueError


print(min_max(array1))
print(min_max(array2))
print(min_max(array3))
print(min_max(array4))
# print(min_max(array5))

# 2
array1 = [3, 1, 2, 1, 3]
array2 = [-1, -1, 0, 2, 2]
array3 = [1.0, 1, 2.5, 2.5, 0]
array4 = []


def unique_sorted(nums: list[float | int]):
    return sorted(set(nums))


print(
    unique_sorted(array1),
    unique_sorted(array2),
    unique_sorted(array3),
    unique_sorted(array4),
)
# 3
array1 = [[1, 2], [3, 4]]
array2 = [[1, 2], (3, 4, 5)]
array3 = [[1], [], [2, 3]]
array4 = [[1, 2], "ab"]


def flatten(mat: list[list | tuple]):
    answer = []
    for n in mat:
        if isinstance(n, list) or isinstance(n, tuple):
            for y in n:
                answer += [y]
        else:
            raise TypeError
    return answer


print(flatten(array1))
print(flatten(array2))
print(flatten(array3))
print(flatten(array4))
