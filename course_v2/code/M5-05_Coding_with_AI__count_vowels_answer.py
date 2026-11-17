# M5-05_Coding_with_AI - count_vowels.py
def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count

print(count_vowels("Ziggy"))
print(count_vowels("APPLE"))
