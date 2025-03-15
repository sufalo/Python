def reverse(str):
    rev_str = ""
    n = len(str) - 1

    for i in range(n, -1, -1):
        rev_str += str[i]

    return rev_str
    
str = "Przykładowy tekst"
print(reverse(str))