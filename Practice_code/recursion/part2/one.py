def sortedArr(arr):
    if len(arr) > 1:

        return arr[0] < arr[1] and sortedArr(arr[2:])
    
    else:
        return True

funBol = sortedArr([1,2,3,5,7,8,9])
print(funBol)