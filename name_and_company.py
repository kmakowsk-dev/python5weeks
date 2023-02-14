name = input('input your name: ')
company = input('input company name: ')

if name == 'Krzysztof' and company == 'Credit Suisse':
    print ('you must be me!')
elif name == 'Krzysztof' and company != 'Credit Suisse':
    print (f'{name}, great name, terrible company!')
elif company == 'Credit Suisse' and name != 'Krzysztof':
    print ('you must be my colleague!')
else:
    print ('terrible name, terrible company!')