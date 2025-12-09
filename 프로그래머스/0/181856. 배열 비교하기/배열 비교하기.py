def solution(arr1, arr2):
    a = 0
    b = 0
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    else:
        arr1_result = sum(arr1)
        arr2_result = sum(arr2)
        if arr1_result > arr2_result:
            return 1
        elif arr1_result < arr2_result:
            return -1
        else:
            return 0
