#Code for understanding While loop

'''
count = 10;
while count >= 1:
  print("Still high!")
  count -=1
'''


# Little complicated example of mine, but deep insight
name = ['sravan', 'anusha']
x = 'sravan'

while x in name:
    if x is 'sravan':
        print(x + 'step 1')
        x = 'anusha'
        print ("Name changed")
    elif x is 'anusha':
        print(x + 'step 2')
        x = 'dhoni'
        print('Again name changed')
    else:
        print(x) #This doesn't get printed because if not present in name list
                 # while condition is not satisfied
