# Q- Finding the target on a Infinite array

def main():
    arr = [3,5,7,9,10,90,100,130,140,160,170]
    target = 200

    return indexS(arr, target)

def indexS(arr, target):
    start = 0
    end = 1

    while target > arr[end]:
        newStart = end + 1
        end = end + (end - start + 1) * 2
        start = newStart

    return searchIndex(arr,target,start,end)

def searchIndex(arr,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1

print(main())
