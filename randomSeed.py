import random as rnd
from typing import List as Lst
import argparse

def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    for divisor in range(2, int(value**0.5) + 1):
        if value % divisor == 0:
            return False
    return True

def generate_primes(count: int) -> Lst[int]:
    prime_numbers_list = []
    candidate = 2
    while len(prime_numbers_list) < count:
        if is_prime(candidate):
            prime_numbers_list.append(candidate)
        candidate += 1
    return prime_numbers_list

def calculate_checksum(numbers: Lst[int]) -> int:
    checksum_result = 0
    for num in numbers:
        checksum_result += num
        checksum_result = (checksum_result * 113) % 10000007
    return checksum_result

def process_pipeline(count: int, seed: int) -> int:
    prime_numbers = generate_primes(count)
    rnd.seed(seed)
    rnd.shuffle(prime_numbers)
    
    for number in prime_numbers:
        print(number)
    
    return calculate_checksum(prime_numbers)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Генерация простых чисел и вычисление контрольной суммы.')
    parser.add_argument('count', type=int, help='Количество простых чисел для генерации')
    parser.add_argument('seed', type=int, help='Начальное значение для генерации случайных чисел')
    
    args = parser.parse_args()
    
    result = process_pipeline(args.count, args.seed)
    print(f"Контрольная сумма: {result}")
