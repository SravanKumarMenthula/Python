#Code for understanding While loop

'''
count = 10;
while count >= 1:
  print(count,"Still high!")
  count -=1
'''


# Little complicated example of mine, but deep insight
name = ['sravan', 'dhoni', 'raina']
x = 'sravan'

while x in name:
    if x is 'sravan':
        print(x + 'step 1')
        x = 'dhoni'
        print ("Name changed")
    elif x is 'dhoni':
        print(x + 'step 2')
        x = 'raina'
        print('Again name changed')
    elif x is 'raina':
        print(x+'step 3')
        x = 'kohli'
        print('Again name changed')
    else:
        print(x) #This doesn't get printed because if not present in name list
                 # while condition is not satisfied

