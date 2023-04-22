arr = [
    [18,9,12],
    [36,-4,91],
    [44,33,16]
]

target = 91

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if target == arr[i][j]:
            print([i,j])