class ObjectExample:  
    def __init__(self, dict_arg):  
        self.__dict__.update(dict_arg)

dict_json = {
        "aa": 'A',
        "bb": 'B',
        "cc": 'C'
        }

oe = ObjectExample(dict_json)
print oe.aa
print oe.bb
print oe.cc
