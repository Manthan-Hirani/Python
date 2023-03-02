import numpy as np

def trans(arr):
    arr = np.array(arr)
    return arr.transpose()

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(trans(arr))