def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str(str_number.replace('0', ''))
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result1 = get_multiplied_digits(int('40203'))
print(result1)
