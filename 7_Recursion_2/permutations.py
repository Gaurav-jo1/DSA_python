def permutations(process="", unprocess="abc"):
    if not unprocess:
        return [process]

    permutation_list = []

    for i in range(0, len(process) + 1):
        new_permutation = process[:i] + unprocess[0] + process[i:]
        permutation_list += permutations(process=new_permutation, unprocess=unprocess[1:])

    return permutation_list

print("Permutations List =",permutations())
