import random

# test branch

def bubble_sort(number):
    len_numbers = len(number) - 1
    i = 0
    while i < len_numbers:
        if number[i] > number[i+1]:
            random.shuffle(number)
            i = 0
        else:
            i += 1
    return number


num = [random.randint(0, 100) for _ in range(5)]
print(bubble_sort(num))