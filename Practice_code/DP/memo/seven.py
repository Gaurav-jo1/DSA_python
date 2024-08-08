from typing import List

def allConstruct(target: str, wordBank: List[str]) -> List[List[str]]:
    memo = {}
    def construct(target: str) -> List[List[str]]:
        if target in memo:
            return memo[target]
        if target == "":
            return [[]]

        all_ways = []

        for word in wordBank:
            if target.startswith(word):
                suffix = target[len(word):]
                suffix_ways = construct(suffix)
                target_ways = [[word] + way for way in suffix_ways]
                all_ways.extend(target_ways)

        memo[target] = all_ways
        return all_ways

    return construct(target)

# Example usage:
result = allConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
print(result)
