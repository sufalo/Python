def czy_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    return sorted(s1) == sorted(s2)

print(czy_anagram("listen", "silent"))
print(czy_anagram("Tom Marvolo Riddle", "I am Lord Voldemort"))
print(czy_anagram("hello", "world"))
