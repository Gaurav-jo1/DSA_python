def revNum(num, rev_num:int=None):

    if num > 0:
        if rev_num is None:
            rev_num = str(num % 10)
        else:
            rev_num = rev_num + str(num % 10)

        return revNum(num= num // 10, rev_num = rev_num)
    
    else:
        return rev_num

    
print(revNum(1924))