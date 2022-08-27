# raise NameError('HiThere')

try:
    raise NameError('hi')
except NameError:
    print('an exception flew by!')
    raise