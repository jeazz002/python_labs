def transpose(mat: list[list[float | int]]):
    res=[list(x) for x in zip(*mat)]
    for row in mat:
        if len(mat[0])!=len(row):
            raise ValueError
    return res
array1=[[1,2,3]]
array2=[[1],[2],[3]]
array3=[[1,2],[3,4]]
array4=[]
array5=[[1, 2], [3]]
print(transpose(array1))
print(transpose(array2))
print(transpose(array3))
print(transpose(array4))
print(transpose(array5))