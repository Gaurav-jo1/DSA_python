# Write a function `allConstruct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return a 2D array containing all of the ways that the 'target` can be constructed by concatenating elements of the `wordBank` array. Each element of the 2D array should represent one combination that constructs the `target`.
# You may reuse elements of wordBank as many times as needed.


class allConstruct:
    def __init__(self) -> None:
        self.memo = {}

    def construct(self, target: str, wordBank: list[str]) -> list[list[str]]:
        if target in self.memo:
            return self.memo[target]

        if not target:
            return [[]]

        results = []

        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                suffixWays = self.construct(suffix, wordBank)
                if len(suffixWays) != 0:
                    for way in suffixWays:
                        results.append([word] + way)

        self.memo[target] = results
        return results

# Example usage
print(allConstruct().construct("purple", ["purp", "p", "ur", "le", "purpl"]))




# print(allConstruct().construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct().construct("purple", ["purp", "p", "ur", "le", "purpl"]))
# print(allConstruct().construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
# print(allConstruct().construct("aaaaaaaaaaaaaaaaaaaaaaz", ["a", "aaaa", "aaaaaa", "aaaaaaa"]))
