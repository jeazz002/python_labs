# 1
def transpose(mat: list[list[float | int]]):
    res = [list(x) for x in zip(*mat)]
    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
    return res


array1 = [[1, 2, 3]]
array2 = [[1], [2], [3]]
array3 = [[1, 2], [3, 4]]
array4 = []
array5 = [[1, 2], [3]]
print(transpose(array1))
print(transpose(array2))
print(transpose(array3))
print(transpose(array4))
# print(transpose(array5))
# 2
array1 = [[1, 2, 3], [4, 5, 6]]
array2 = [[-1, 1], [10, -10]]
array3 = [[0, 0], [0, 0]]
array4 = [[1, 2], [3]]


def row_sums(mat: list[list[float | int]]):
    res = [sum(x) for x in mat]
    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
    return res


print(row_sums(array1))
print(row_sums(array2))
print(row_sums(array3))
print(row_sums(array4))
# 3
array1 = [[1, 2, 3], [4, 5, 6]]
array2 = [[-1, 1], [10, -10]]
array3 = [[0, 0], [0, 0]]
array4 = [[1, 2], [3]]


def col_sums(mat: list[list[float | int]]):
    res = [sum(x) for x in zip(*mat)]
    for row in mat:
        if len(mat[0]) != len(row):
            raise ValueError
    return res


print(col_sums(array1))
print(col_sums(array2))
print(col_sums(array3))
print(col_sums(array4))
