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


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass
    v_ticket=list(str(ticket_number))
    v_len=len(v_ticket)
    v_left_side=0
    v_right_side=0
    if v_len==6:
        for i in range(6):
            if i <= 3:
                v_left_side += int(v_ticket[i])
            else:
                v_right_side += int(v_ticket[i])
        if v_left_side == v_right_side:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))