def transposition_cipher(text: str, key: int) -> str:
    if key > len(text):
        return text

    text_list = list(text)
    
    for i in range(0, len(text), key):
        if i + key < len(text):
            text_list[i], text_list[i + key] = text_list[i + key], text_list[i]
    
    return ''.join(text_list)

text = "abcdefghij"
key = 3
result = transposition_cipher(text, key)
print(result)
