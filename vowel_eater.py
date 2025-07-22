user_input = input("Enter a word: ")
vowels = ['a','e','i','o','u']
result = ''

for letter in user_input.lower():
    if letter in vowels:
        continue
    else:
        result += letter
print(result)