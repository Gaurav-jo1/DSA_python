def SkipCharacter(letters, target, steps=0):
    if steps >= len(letters):
        return letters
    else:
        # check if the target is present 
        if letters[steps] == target:
            letters = letters[:steps] + letters[steps:]

            return SkipCharacter(letters, target, steps + 1)
        else:
            return SkipCharacter(letters, target, steps + 1)


print(SkipCharacter("baccad", "c"))