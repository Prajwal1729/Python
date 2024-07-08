def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [100,30,10,11,12,5,2,1,300,6]

bubbleSort(arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
print()