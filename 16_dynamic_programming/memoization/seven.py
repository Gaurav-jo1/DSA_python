# Write a function `count Construct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return the number of ways that the `target can be constructed by concatenating elements of the `wordBank array.
# You may reuse elements of `wordBank` as many times as needed.


class countConstruct:
    def __init__(self) -> None:
        self.memo = {}

    def can_construct(self, target: str, wordBank: list[str], count: int = 0) -> int:
        if target in self.memo:
            return self.memo[target]

        if not target:
            return 1

        for word in wordBank:
            if target.startswith(word):
                remainder = target[len(word):]
                remaining = self.can_construct(remainder, wordBank)
                if remaining != 0:
                    self.memo[remainder] = remaining
                    count += remaining

        return count


canC = countConstruct()
print(canC.can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(canC.can_construct("purple", ["purp", "p", "ur", "le", "purpl"]))


# class countConstruct:
#     def __init__(self) -> None:
#         self.memo = {}
#         self.count = 0

#     def can_construct(self, target: str, wordBank: list[str]) -> int:
#         if target in self.memo:
#             self.count += 1
#             return self.memo[target]

#         if not target:
#             self.count += 1
#             return 1

#         for word in wordBank:
#             if target.startswith(word):
#                 remaining = self.can_construct(target[len(word):], wordBank)
#                 if remaining != 0:
#                     self.memo[target] = remaining

#         return self.count


# canC = countConstruct()
# print(canC.can_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
