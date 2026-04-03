user_input = input("Enter a string:>>")
vowel_count = 0
consonant_count = 0

for char in user_input.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
    else:
        consonant_count += 1

print("Number of vowels in the string:>>", vowel_count)
print("Number of consonants in the string:>>", consonant_count)

print("Total number of characters in the string:>>", len(user_input))