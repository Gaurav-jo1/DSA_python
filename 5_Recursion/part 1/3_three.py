# Reverse a number

#  1'st Method
def RevNum(n):

    if n == 0:
        return 0
    
    last_num = n % 10

    module = 1

    while (n // module) >= 9 :

        module = module * 10 
        n  // module

    return (last_num * module) + RevNum((n - last_num) // 10)

print(RevNum(1824)) 
