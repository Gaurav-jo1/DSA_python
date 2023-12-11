def allConstruct(target, wordBank):
    array = [[] for _ in range(len(target) + 1)]
    array[0] = [[]]

    for i in range(len(target) + 1):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                newCombinations = [subArray + [word] for subArray in array[i]]
                array[i + len(word)].extend(newCombinations)

    return array[-1]


print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("aaaaaaaaaaz", ["a", "aa", "aaaa", "aaaaaa"]))
