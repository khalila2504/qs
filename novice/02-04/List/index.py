shoplist = ['apple', 'mango', 'watermelon', 'banana']
print('i have', len(shoplist), 'items to purchase')
print('these items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\ni also have to buy nugget')
shoplist.append('nugget')
print('my shopping list is now', shoplist)
print('i will sort my list now')
shoplist.sort()
print('sorted shopping list is', shoplist)
print('the first item i will buy is', shoplist)
print('the first item i will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('i bought the', olditem)
print('my shopping list is now', shoplist)