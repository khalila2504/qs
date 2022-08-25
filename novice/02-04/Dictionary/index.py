ab = {
    'swaroop': 'swaroop@swaroopch.com',
    'lary': 'larry@wall.org',
    'matsumoto': 'matz@ruby-lang.org',
    'spammer': 'spammer@hotmail.com'
}

print("swaroop's address is", ab['swaroop'])
del ab['spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])