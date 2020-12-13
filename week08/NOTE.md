学习笔记

Bubble Sort

def BubbleSort(arr):
    if not arr:
        return False
    n = len(arr)
    while n > 0:
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        n -= 1
    return arr
