# Return the list without passing the argument 

def arrList(arr, target, ind=0):

    answer_list = []
    
    if len(arr) == ind:
        return answer_list

    if arr[ind] == target:
        answer_list.append(ind)

    return answer_list + arrList(arr, target, ind = ind + 1)

print(arrList(arr=[1, 2, 3, 4, 4, 8], target=4))