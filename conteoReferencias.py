
l1 = [1, 2, 3, 4, 5]

l2 = l1
l3 = l1.copy()

print(f'l1: {l1} --> id(l1): {id(l1)}')
print(f'l2: {l2} --> id(l2): {id(l2)}')
print(f'l3: {l3} --> id(l3): {id(l3)}')

print(f'l1 == l2? {l1 == l2}')
print(f'l1 == l3? {l1 == l3}')


print(f'l1 is l2? {l1 is l2}')
print(f'l1 is l3? {l1 is l3}')