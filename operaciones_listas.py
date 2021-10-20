a = [8,2,3,5,1,6,9,9]
b = ['a','b','c']

total= sum(a)
print('Total: ,',total)

a.append(9)
a.append(8)
print(a)

a.pop()
print(a)

a.sort(reverse= True)
print(a)

a.extend(b)
print(a)


print('cuenta de 9', a.count(9))

print('indice de c', a.index('c'))


a.insert(5,'nuevo')
print(a)

a.remove(5)
print(a)



a.clear()
print(a)
