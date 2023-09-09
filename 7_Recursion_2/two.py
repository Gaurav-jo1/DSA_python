def SkipString(the_str:str, rem_str="apple"):
    if not the_str:
        return ""

    if the_str.startswith(rem_str):
        return SkipString(the_str[5:])

    return the_str[0] + SkipString(the_str[1:])


print(SkipString("bacapplecad"))
