#This code helps us to understand functions in python
'''
#1
def odd_even(number):
  if number%2 == 0:
    print("The Number given is even!")
  else:
    print("The Number given is Odd!")

odd_even(4)
odd_even(3)
'''

'''
#2
number = 9 # this number is differnt from the number in function
def funtion_to_return_integer(number):
    return number**2
number = number+1
print(funtion_to_return_integer(2))
print(funtion_to_return_integer(25))
print(number)
'''

#3

def return_gender(sex = 'unknown'):
    if sex == 'm':
        return 'Male'
    elif sex == 'f':
        return 'Female'
    else:
        return sex

print(return_gender())
print(return_gender('m'))
print(return_gender('f'))
