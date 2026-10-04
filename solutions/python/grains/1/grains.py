def square(number):
    
    if number >=1 and number <=64:
        square_rice_number = 2 ** (number - 1)
        return square_rice_number
    else:
        raise ValueError("square must be between 1 and 64")


def total():
    total = 2 ** 64 - 1
    return total
