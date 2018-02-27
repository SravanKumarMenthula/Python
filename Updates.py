# set.add() for sets
# array.append() for arrays
# dictionary.update() for Dictionarys


Players = ['Dhoni', 'Kohli', 'Kohli','Rohit']

Groceries = { 'Milk', 'Milk','Apples', 'Oranges'}

dictionary = {'Apples' : 'Good for Health',
              'Apples' : 'Good for Health',
              'Oranges': 'Vitamin C'}

for p in Players:
    print(p)
print("-------------")
for g in Groceries:
    print(g)
print("-------------")
for k,v in dictionary.items():
    print(k +':'+v)

print("Now updating the array, set and Dictionary......")

Players.append("Dhawan")

for p in Players:
    print(p)
print("-------------")

Players = Players + ["Bhuvi"]

for p in Players:
    print(p)
print("-------------")
Groceries.add("Lemons")
for g in Groceries:
    print(g)
print("-------------")
dictionary.update({'Lemons':'Anti-Oxidant'})
for k,v in dictionary.items():
    print(k +':'+v)
