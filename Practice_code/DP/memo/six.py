# Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return a boolean indicating whether or not the `target can be constructed by concatenating elements of the `wordBank array.
# You may reuse elements of wordBank` as many times as needed.

from typing import List


class canConstruct:

    def __init__(self) -> None:
        self.memo = {}

    def can_construct(self, target: str, array: List[str], sum_str: str = ""):
        if target in self.memo:
            return self.memo[target]

        if target == "":
            return True

        for word in array:
            if target.startswith(word):
                if self.can_construct(target[len(word) :], array):
                    self.memo[target] = True
                    return True

        self.memo[target] = False
        return self.memo[target]


# print(
#     canConstruct().can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
# )  # True

print(
    canConstruct().can_construct(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
)  # False
# print(
#     canConstruct().can_construct(
#         "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]
#     )
# )  # True
# print(
#     canConstruct().can_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee"],
#     )
# )  # False
