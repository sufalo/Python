def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_selector(numbers: list[int]) -> list[int]:
    return [num for num in numbers if is_prime(num)]

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = prime_selector(numbers)
print(result)
