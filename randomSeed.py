import random as rnd
from typing import List as Lst

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

def process_pipeline() -> int:
    prime_numbers = generate_primes(1000)
    rnd.seed(100)
    rnd.shuffle(prime_numbers)
    return calculate_checksum(prime_numbers)


if __name__ == "__main__":
    result = process_pipeline()
    print(f"Контрольная сумма: {result}")
