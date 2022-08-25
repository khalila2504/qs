shoplist = ['keju', 'yogurt', 'susu', 'kue']
name = 'aya'

print('item 0 is', shoplist[0])
print('item 1 is', shoplist[1])
print('item 2 is', shoplist[2])
print('item 3 is', shoplist[3])
print('item -1 is', shoplist[-1])
print('item -2 is', shoplist[-2])
print('character 0 is', name[0])

print('item 1 to 3 is', shoplist[1:3])
print('item 2 to end is', shoplist[2:1])
print('Item 1 to -1 is', shoplist[1:-1])
print('Item start to end is', shoplist[:])

print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

shoplist = ['chiki', 'taro', 'potato', 'lays']
print(shoplist[::1])

print(shoplist[::2])

print(shoplist[::3])

print(shoplist[::-1])