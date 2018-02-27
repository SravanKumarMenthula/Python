
#Program to get the understanding of For loop.

#1: Traversal through list

players = ['Dhoni', 'Kohli', 'Rohit', 'Bumrah', 'Bhuvi']

for p in players:
    print(p + ' country: India',len(p))
    #print(len(p))


#2:
'''
for i in range(10):
    print (i)
'''
#3:
'''
for i in range(1,10,2):
    print(i, end =' ')  #makes the code to print values in one row
                        #rather than making a new line
'''

#4 Using the Break statement:
'''
magic = 26

for i in range(101):
    if i == magic:
        print("The magic number is: ", i)
        print("You won't traverse the loop from now on")
        break
    else: print(i,":" + "You haven't reached the number yet!")
'''
