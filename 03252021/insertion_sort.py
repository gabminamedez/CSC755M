def insertionSort(arr, N):
    count = 0
    for j in range(1, N):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            count += 1
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key

    print("Final Count: " + str(count))
    return arr

arr1 = [10, 2, 3, 4, 1, 5, 7, 6, 8, 9]
arr2 = [1, 2, 2, 4, 1, 5, 2, 8, 8, 2]
arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(insertionSort(arr1, len(arr1)))
print(insertionSort(arr2, len(arr2)))
print(insertionSort(arr3, len(arr3)))