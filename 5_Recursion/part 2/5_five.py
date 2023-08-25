def rotated_binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    
    # If the left half is normally sorted
    if arr[low] <= arr[mid]:
        if arr[low] <= target <= arr[mid]:
            return rotated_binary_search(arr, target, low, mid - 1)
        else:
            return rotated_binary_search(arr, target, mid + 1, high)
    
    # If the right half is normally sorted
    if arr[mid] <= target <= arr[high]:
        return rotated_binary_search(arr, target, mid + 1, high)
    else:
        return rotated_binary_search(arr, target, low, mid - 1)

def search_in_rotated_array(arr, target):
    return rotated_binary_search(arr, target, 0, len(arr) - 1)

# Example usage
rotated_array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
target = 6
result = search_in_rotated_array(rotated_array, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print("Element not found")
