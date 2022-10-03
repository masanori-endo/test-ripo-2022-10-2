import random

def bogo_sort(numbers):
    len_numbers = len(numbers) - 1
    count = 0
    i = 0
    while i < len_numbers:
        count += 1
        if numbers[i] > numbers[i+1]:
            random.shuffle(numbers)
            i = 0
        else:
            i += 1
    print(f'count = {count}')
    return numbers

s = bogo_sort

nums = [random.randint(0, 1000) for i in range(5)]
print(s(nums))
print(bogo_sort(nums))

