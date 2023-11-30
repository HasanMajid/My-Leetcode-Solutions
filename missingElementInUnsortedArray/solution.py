
def solution(arr):
    newArr = [0] * len(arr)
    for x in arr:
        newArr[x-1] = 1
    for i in range(len(arr)):
        if newArr[i] == 0:
            print(i + 1)
            return i + 1
    return -1
solution([1, 3, 2, 5, 5])