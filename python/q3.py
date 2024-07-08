def insertionSort(arr):

    for i in range(1,len(arr)):
        k = arr[i]
        j = i-1

        while j >=0 and k<arr[j]:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = k
    
    return arr


arr = [12,5,7,2,100,34]
insertionSort(arr)

print(arr)      