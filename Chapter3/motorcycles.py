motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles2 = []

motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('suzuki')

print(motorcycles2)

motorcycles2.insert(0, 'ducati')
print(motorcycles2)

del motorcycles2[0]
print(motorcycles2)

del motorcycles2[1]
print(motorcycles2)
print()

motorcycles3 = ['honda', 'yamaha', 'suzuki']
print(motorcycles3)

popped_motorcycle = motorcycles3.pop()
print(motorcycles3)
print(popped_motorcycle)
print()

motorcycles4 = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles4.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")