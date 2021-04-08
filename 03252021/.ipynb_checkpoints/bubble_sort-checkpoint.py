def bubbleSort(arr, N):
    count = 0
    for i in range(N, 0, -1):
        for j in range(1, N):
            count += 1
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    print("Final Count: " + str(count))
    return arr

arr1 = [10, 2, 3, 4, 1, 5, 7, 6, 8, 9]
arr2 = [1, 2, 2, 4, 1, 5, 2, 8, 8, 2]
arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(bubbleSort(arr1, len(arr1)))
print(bubbleSort(arr2, len(arr2)))
print(bubbleSort(arr3, len(arr3)))