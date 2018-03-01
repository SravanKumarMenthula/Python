import json
import re

class Car():

    Brand =""
    Model =""

    @classmethod
    def get_json(cls):
        data = json.load(open('dict_info.json'))
        return data

    @classmethod
    def get_blue_print(cls):
        bp_items = []
        file1 = open('bp.txt','r')
        file_line  = file1.readline()
        while file_line != '':
            file_line = file_line.strip()
            bp_items.append(file_line)
            file_line = file1 .readline()
        return bp_items



    @classmethod
    def get_dict_info(cls):
        data = cls.get_json()
        bp = cls.get_blue_print()
        #print(bp[0])
        count = 0
        for k in data.keys():
            for v in data[k].keys():
                r =re.compile(bp[count])
                count = count + 1
                if r.match(data[k][v]):
                    print('Fine')
                else:
                    print('Not Fine!')
