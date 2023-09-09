def SkipAppString(the_str:str, rem_str="app"):
    if not the_str:
        return ""

    if the_str.startswith(rem_str) and not the_str.startswith("apple"):
        return SkipAppString(the_str[3:])

    return the_str[0] + SkipAppString(the_str[1:])


print(SkipAppString("bacapplcad"))
