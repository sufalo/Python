def most_frequent_element(data: list):
    frequency = {}
    
    for element in data:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    
    most_frequent = None
    max_count = 0
    
    for element, count in frequency.items():
        if count > max_count:
            most_frequent = element
            max_count = count
    
    return most_frequent

data1 = [1, 2, 2, 3, 3, 3, 4, 5]
data2 = ["apple", "banana", "apple", "apple", "banana", "cherry"]

print(most_frequent_element(data1))
print(most_frequent_element(data2))
