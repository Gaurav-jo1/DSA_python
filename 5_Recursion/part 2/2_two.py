# Linear Search

def LinSearch(arr, target, ind=0):

    if len(arr) - 1 == ind:
        return print("Target Not to be Found")
    
    elif arr[ind] == target:
        return print(f"Target found at Index {ind}")
    
    LinSearch(arr, target, ind= ind + 1)

LinSearch([3,2,1,18,9], target=18)