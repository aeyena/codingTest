def solution(sizes):
    arr1 = list(map(lambda x:x[0], sizes))
    arr2 = list(map(lambda x:x[1], sizes))
    answer = 1
    if (max(arr1)>=max(arr2)):
        answer *= max(arr1)
        for i in range(len(arr2)):
            if arr2[i]>arr1[i]:
                arr2[i] = arr1[i]
        answer *= max(arr2)
    else:
        answer *= max(arr2)
        for i in range(len(arr1)):
            if arr1[i]>arr2[i]:
                arr1[i] = arr2[i]
        answer *= max(arr1)
    return answer