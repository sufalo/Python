import re

def readability_score(text: str) -> float:
    sentence_endings = re.findall(r'[.!?]', text)
    num_sentences = len(sentence_endings)
    
    words = text.split()
    num_words = len(words)
    
    def count_syllables(word):
        vowels = "aeiouyAEIOUY"
        count = 0
        for letter in word:
            if letter in vowels:
                count += 1
        return count
    
    num_syllables = sum(count_syllables(word) for word in words)
    
    avg_words_per_sentence = num_words / num_sentences if num_sentences else 0
    avg_syllables_per_word = num_syllables / num_words if num_words else 0
    
    readability = avg_words_per_sentence + avg_syllables_per_word
    
    return readability

text = "This is a simple sentence. Here is another one! Do you understand?"
score = readability_score(text)
print(f"Readability score: {score}")
