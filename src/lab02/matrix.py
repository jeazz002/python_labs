#1
def transpose(mat: list[list[float | int]]):
    return [list(x) for x in zip(*mat)]
array1=[[1,2,3]]
array2=[[1],[2],[3]]
array3=[[1,2],[3,4]]
print(transpose(array3),transpose(array2),transpose(array1))
#2
array1=[[1,2,3],[4,5,6]]
array2=[[-1,1],[10,-10]]
def row_sums(mat: list[list[float | int]]):
    res=[sum(x) for x in mat]
    return res
print(row_sums(array1),row_sums(array2))
#3
array1=[[1,2,3],[4,5,6]]
array2=[[-1,1],[10,-10]]
array3=[[0,0],[0,0]]
def col_sums(mat: list[list[float | int]]):
    return [sum(x) for x in zip(*mat)]
print(col_sums(array1),col_sums(array2), col_sums(array3))