import random

def prime_number_v1(number):
    prime = []
    for i in range(2, number):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime



if __name__ == '__main__':
    print(prime_number_v1(100))
    
