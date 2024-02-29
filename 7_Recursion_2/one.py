def SkipCharacter(the_str):
    if the_str == "":
        return ""

    if the_str[0] != "a":
        return the_str[0] + SkipCharacter(the_str[1:])

    return SkipCharacter(the_str[1:])


print(SkipCharacter("baccad"))
