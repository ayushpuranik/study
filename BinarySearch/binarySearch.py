# Enter your code here...
import math


def binSearch(arr, num):
    return binarySearch(arr, num, 0, len(arr) - 1)


def binarySearch(arr, num, fIndex, lIndex):
    if arr[fIndex] == num:
        return fIndex
    if arr[lIndex] == num:
        return lIndex

    mid = math.floor((fIndex + lIndex) / 2)
    print(fIndex, mid, lIndex)
    if fIndex < mid and mid < lIndex:
        if arr[mid] < num:
            return binarySearch(arr, num, mid, lIndex)
        elif arr[mid] >= num:
            return binarySearch(arr, num, fIndex, mid)

    return -1;


print(binSearch([1, 2, 3, 4, 5, 10, 40], 1))