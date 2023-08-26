def insert(arr, n):
    if n <= 1:
        return
    
    insert(arr, n - 1)
    
    last = arr[n - 1]
    j = n - 2
    
    def shift_elements(j):
        if j < 0 or arr[j] <= last:
            arr[j + 1] = last
            return
        arr[j + 1] = arr[j]
        shift_elements(j - 1)
    
    shift_elements(j)

def insertion_sort_recursive(arr):
    insert(arr, len(arr))

# Example usage
arr = [12, 11, 13, 5, 6]
insertion_sort_recursive(arr)
print("Sorted array:", arr)
