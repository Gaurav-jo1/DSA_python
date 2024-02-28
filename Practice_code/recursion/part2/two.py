# Array List

def ArrList(arr,target, ptr=0):

    if ptr >= len(arr) - 1:
        return []
    
    if arr[ptr] == target:
        return [ptr] + ArrList(arr, target, ptr + 1)
    else:
        return ArrList(arr, target, ptr + 1)

print(ArrList([1, 2, 3, 4, 4, 8], 4))