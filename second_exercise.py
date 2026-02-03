import random



def get_numbers_ticket(min, max, quantity):
    if min <= 0:
        return []
    elif max > 1000:
        return []
    elif quantity > (max - min + 1):
        return []
    else:
        tick_nums = random.sample(range(min, max+1), quantity)
        tick_nums.sort()
        return tick_nums

result = get_numbers_ticket(1, 49, 6)
print('Віші лотерейні числа: ', result)
