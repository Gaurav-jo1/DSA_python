def canConstruct(target, wordBank):
    array = [False for _ in range(len(target) + 1)]
    array[0] = True

    for i in range(len(target) + 1):
        if array[i]:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    array[i + len(word)] = True

    return array[-1]


# print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeeee"]))
