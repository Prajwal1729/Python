def max_amount_water(arr):
    l = 0
    r = len(arr) - 1
    maxArea = 0
    while l < r:
        currArea = min(arr[l],arr[r]) * (r-l)
        maxArea = max(maxArea,currArea)
 
        if arr[l] < arr[r]:
            l+=1
        else:
            r-=1

    return maxArea


arr = [1,8,6,2,5,4,8,6,7]
print(max_amount_water(arr))