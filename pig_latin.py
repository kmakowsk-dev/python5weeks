word = input('Enter your word: ')

if word[0] in 'aeiou':
    print (f'in ping latin it is: {word}way')
else: 
    first_letter=word[0]
    word = word[1:] + first_letter + 'ay'
    print (word)