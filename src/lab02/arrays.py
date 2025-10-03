#1
array1 = [3, -1, 5, 5, 0]
array2 = [42]
array3 = [-5, -2, -9]
array4 = [1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]):
    n =[a for a in nums]
    return min(nums),max(nums)
print(min_max(array1), min_max(array2), min_max(array3), min_max(array4))
#2
array1 = [3, 1, 2, 1, 3]
array2 = [-1, -1, 0, 2, 2]
array3 = [1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]):
    n =[a for a in nums]
    return sorted(set(nums))
print(unique_sorted(array1), unique_sorted(array2), unique_sorted(array3),)
#3
array1 = [[1, 2], [3, 4]]
array2 = [[1, 2], (3, 4, 5)]
array3 = [[1], [], [2, 3]]
def flatten(mat: list[list | tuple]):
    answer = []
    for n in mat:
        for y in n:
            answer += [y]
    return answer
print(flatten(array1), flatten(array2), flatten(array3),)