import pytest
from randomSeed import is_prime, generate_primes, calculate_checksum, process_pipeline

@pytest.mark.parametrize("number,expected", [
    (2, True),
    (3, True),
    (4, False),
    (13, True),
    (20, False)
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected


def test_generate_primes_length():
    prime_numbers_list = generate_primes(1000)
    assert len(prime_numbers_list) == 1000

def test_generate_primes_content():
    prime_numbers_list = generate_primes(10)
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert prime_numbers_list == expected_primes

def test_calculate_checksum():
    numbers = [1, 2, 6, 24]
    assert calculate_checksum(numbers) == 6012369

def test_process_pipeline():
    result = process_pipeline()
    assert result == 7785816
