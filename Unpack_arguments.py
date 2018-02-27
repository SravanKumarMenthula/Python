#Unpacking the arguments

def strike_rate(runs, balls):
  strikerate = (runs/balls)*100
  return strikerate



Dhoni = [90, 100]
Kohli = [93,100]
Rohit = [91,100]

print(strike_rate(Dhoni[0], Dhoni[1]))
print(strike_rate(*Dhoni)) #Both are same

print(strike_rate(*Kohli))
print(strike_rate(*Rohit))
