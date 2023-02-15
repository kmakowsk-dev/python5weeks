vowels = 0
consonants = 0

s = input('enter a string: ').strip()

for one_char in s:
    if one_char in 'aeiou':
        vowels += 1
    elif one_char in 'bcdfghjklmnpqrstwxyz':
        consonants += 1
    else:
        print(f'ignoring {one_char} ')

print(f'vowels = {vowels}')
print(f'consonants = {consonants}')