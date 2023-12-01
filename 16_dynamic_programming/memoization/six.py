# Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return a boolean indicating whether or not the `target can be constructed by concatenating elements of the `wordBank array.
# You may reuse elements of wordBank` as many times as needed.


class canConstruct:
    def __init__(self) -> None:
        pass

    def can_construct(self, target: str, wordBank: list[str]) -> bool:
        pass
        if not target:
            return True

        for word in wordBank:
            if word in target:
                if self.can_construct(target.replace(word, ""), wordBank):
                    return True

        return False


print(canConstruct().can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
