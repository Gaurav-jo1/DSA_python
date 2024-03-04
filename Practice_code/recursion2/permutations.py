
from typing import List

def permutations(unprocess: str, process: str = "") -> List[str]:
    if not unprocess:
        return [process]

    permutations_list = []

    for i in range(0, len(process) + 1):
        new_proc = process[:i] + unprocess[0] + process[i:]
        permutations_list += permutations(unprocess[1:], new_proc)

    return permutations_list


print(permutations("abc"))
