# No duplicates in Set. If at all, it considers multiple of them as considers

#groceries = {'milk', 'banana','orange','milk'} #set.add() for set
groceries  = [ 'milk', 'oranges'] #array.append() for array
done = 'n'

while done!='y':
  item = input("Enter the item you needed:")
  if item in groceries:
    print("Already in groceries")
  else:
    groceries.append(item)
    print("Added to set")
  done = input("Are you done?(y/n)")

print(groceries)
