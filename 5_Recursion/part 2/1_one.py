# Find Array is Sorted or Not

def sortedArr(n):

    if len(n) == 1:
        return True

    return n[0] < n[1] and sortedArr(n[1:])

funBol = sortedArr([1,2,3,5,7,8,9])
print(funBol)