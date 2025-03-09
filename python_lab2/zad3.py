def longest_increasing_subsequence(sequence:list[int]) -> list[int]:
    max_length = 1
    cnt = 1

    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i - 1]:
            cnt += 1  # Zwiększamy długość bieżącego ciągu rosnącego
        else:
            max_length = max(max_length, cnt)  # Sprawdzamy, czy znaleźliśmy dłuższy ciąg
            cnt = 1  # Resetujemy długość bieżącego ciągu
    
    # Sprawdzamy ostatni ciąg (ponieważ może kończyć się na końcu listy)
    max_length = max(max_length, cnt)
    
    return max_length

sequence = [1, 3, 2, 3, 4, 1, 2, 3, 4, 5]
result = longest_increasing_subsequence(sequence)
print(result)
