def FindSubset(proc="", unproc="abc"):
    if unproc == "":
        print(proc)
        return

    FindSubset(proc + unproc[0], unproc[1:])
    FindSubset(proc, unproc[1:])

# FindSubset()

def ArraySubsets(string, current="", index=0):
    if index == len(string):
        return [[current]]

    subsets_with_char = ArraySubsets(string, current + string[index], index + 1)
    subsets_without_char = ArraySubsets(string, current, index + 1)

    return subsets_with_char + subsets_without_char

print(ArraySubsets("abc"))


def FindSubsetsASCII(string, current="", index=0):
    if index == len(string):
        ascii_values = [ord(char) for char in current]
        print(f"{current}: {ascii_values}")
        return

    FindSubsetsASCII(string, current + string[index], index + 1)
    FindSubsetsASCII(string, current, index + 1)


# FindSubsetsASCII("abc")
