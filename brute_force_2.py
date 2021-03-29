import math
from itertools import permutations
def check_prime_number(number) :
    is_prime = True
    if number == 0 or number == 1:
        is_prime = False
    for i in range(2, int(math.sqrt(number))+1) :
        if number%i == 0 :
            is_prime = False
            break
    return is_prime

def solution(numbers):
    possible_prime_number = []
    for i in range(1, len(numbers)+1):
        possible_numbers = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(possible_numbers)):
            if check_prime_number(int(j)):
                possible_prime_number.append(int(j))

    return len(set(possible_prime_number))

card_list = [1, 2, 3]
print(list(permutations(card_list, 2)))