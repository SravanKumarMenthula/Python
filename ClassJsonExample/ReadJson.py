import CarModule

print("Calling a method which takes the dictionary json file")
p = CarModule.Car()
p.get_dict_info() #only instance can call the instance method
print("Calling a method which takes the list json file")
p.get_list_info()
