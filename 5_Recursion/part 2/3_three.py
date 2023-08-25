#  Return an array List 
def ArrList(arr, target, ind=0, answerList=None):

    if answerList is None:
        answerList = []
        
    if len(arr) == ind:
        return answerList

    elif arr[ind] == target:
        answerList.append(ind)

    return ArrList(arr, target, ind = ind + 1, answerList=answerList)


print(ArrList([1, 2, 3, 4, 4, 8], 4))
