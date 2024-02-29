def subsets(unproc, proc=""):
    if unproc == "":
        print(proc)
        return
    
    subsets(unproc[1:],proc + unproc[0])
    subsets(unproc[1:], proc)

# subsets("abc")

def subsetsArr(unproc, proc=""):
    if unproc == "":
        return [proc]
    
    first = subsetsArr(unproc[1:],proc + unproc[0])
    second = subsetsArr(unproc[1:], proc)

    return first + second

print(subsetsArr("abc"))