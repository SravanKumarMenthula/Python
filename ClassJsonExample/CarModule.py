import json
class Car():
    n_wheels = 4

    @classmethod
    def get_wheels(cls):
        print(cls.n_wheels)

    def __init__(self):
        pass


    def get_list_data(self):
        list_data = json.load(open('list_info.json'))
        return list_data

    def get_dict_data(self):
        dict_data = json.load(open('dict_info.json'))
        return dict_data

    #If the Json has list of dictionaries
    def get_list_info(self):
        list_data = self.get_list_data()
        self.Brand = input("Enter the Brand:")
        self.Model = input("Enter the Model:")
        if self.Brand in list_data.keys(): #Checking whether the Brand is present in the Json file is present
            list1 = list_data[self.Brand]
            logic = 0
            for x in list1:  #Traverse through the list
                if self.Model in x.keys():  #Check whether the model is present in the given Brand.
                    print(x[self.Model])
                    logic = 1 #flaging that we found the desired key
            if logic is 0:
                print("List: Sorry, Info about that Model is Not available")
        else:
            print("List: Sorry, Info about that Brand is Not available")

    #If the Json has dictionary of dictonaries

    def get_dict_info(self):
        dict_data = self.get_dict_data()
        self.Brand = input("Enter the Brand:")
        self.Model = input("Enter the Model:")
        if self.Brand in dict_data.keys():
            if self.Model in dict_data[self.Brand].keys():
                print(dict_data[self.Brand][self.Model])
            else:
                print("Dict: Sorry, Info about that Model is Not available")
        else:
                print("Dict: Sorry, Info about that Brand is Not available")
