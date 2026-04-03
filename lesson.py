user_input = input("Enter a string:>>")
count = 0

for char in user_input.lower():
    if char in ['a', 'e', 'i', 'o', 'u']:
        count +=1


print("Number of vowels in the string:>>", count)