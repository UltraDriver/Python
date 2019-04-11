def my_round(number, ndigits):
    pass
    convert = 10**ndigits
    left = (number * convert % 1) / convert
    trunc_num = number - left
    if left * convert < 0.5:
        return number - left
    else:
        return trunc_num + 1/convert


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

print(my_round(2.0000047, 5))
