def shellSort(arr, N):
    count = 0
    interval = N / 2
    while interval > 0:
        for i in range(interval, N):
            count += 1
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval /= 2

    print("Final Count: " + str(count))
    return arr

arr1 = [10, 2, 3, 4, 1, 5, 7, 6, 8, 9]
arr2 = [1, 2, 2, 4, 1, 5, 2, 8, 8, 2]
arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(shellSort(arr1, len(arr1)))
print(shellSort(arr2, len(arr2)))
print(shellSort(arr3, len(arr3)))