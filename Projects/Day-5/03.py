import numpy as np

def sum(arr):
    arr = np.array(arr)
    return arr.sum(axis=0)

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum(arr))