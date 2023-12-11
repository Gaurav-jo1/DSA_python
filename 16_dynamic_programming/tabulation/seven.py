def countConstruct(target, wordBank):
    array = [0 for _ in range(len(target) + 1)]
    array[0] = 1

    for i in range(len(target) + 1):
        if array[i]:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    array[i + len(word)] += array[i]

    return array[-1]


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(
    countConstruct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["ee", "eeee", "eeeeee", "eeeeee", "eeeeeeee"],
    )
)
