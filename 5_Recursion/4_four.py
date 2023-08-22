# Pallindrome

def pallin(number, accumulator=0):

    if number == 0:
        return accumulator
    
    # Extract the last digit of the number
    last_digit = number % 10
    
    # Build the reversed number using accumulator
    reversed_number = accumulator * 10 + last_digit
    
    # Remove the last digit from the number
    remaining_number = number // 10
    
    # Recursive call with the remaining number and updated accumulator
    number == pallin(remaining_number, reversed_number)

    if number:
        return print("It is a pallindrome")

    return print("Not a pallindrome")

print(pallin(10001))