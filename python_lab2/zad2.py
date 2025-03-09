def round_numbers(numbers: list[int], threshold: int) -> list[int]:
    rounded_numbers = []
    
    for num in numbers:
        if num < threshold:
            rounded_numbers.append((num // 10) * 10)
        else:
            rounded_numbers.append((num + 9) // 10 * 10)
    
    return rounded_numbers

numbers = [23, 45, 78, 62, 5, 99]
threshold = 50
result = round_numbers(numbers, threshold)
print(result)
