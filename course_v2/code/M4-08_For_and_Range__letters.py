# M4-08_For_and_Range - letters.py
word = input("Type a word: ")
for letter in word:
    print(letter.upper(), end=" ")
print()
vowels = 0
for letter in word.lower():
    if letter in "aeiou":
        vowels += 1
print(f"{word} has {len(word)} letters and {vowels} vowels")
