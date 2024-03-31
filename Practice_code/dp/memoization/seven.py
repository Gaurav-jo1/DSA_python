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
                new_target = target.replace(word, "")
                is_construct = self.can_construct(new_target, wordBank)

                if is_construct:
                    self.memo[new_target] = is_construct 
                    count += is_construct

        return count

# print(
#     countConstruct().can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"])
# )  # True

# print(countConstruct().can_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(
    countConstruct().can_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee"],
    )
)  # False