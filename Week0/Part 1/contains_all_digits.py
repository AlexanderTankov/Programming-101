def contains_digits(number, digits):
    for i in digits:
        flag = False
        temp = number
        while temp != 0:
            if temp % 10 == i:
                flag = True
            temp //= 10
        if not flag:
            return False
    return True
