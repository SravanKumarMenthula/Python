#variable number of arguments

def sum(*args):
  total = 0
  for a in args:
    total += a
  print(total)

sum(1)
sum(1,2,4)
#sum(range(4))
