from inspect import getmodule




class Dual:
    ARVALUE = 1000
    def __init__(self, name: str, value: int, s_trin: str):
        self.name = name
        self.value = value
        self.s_trin = s_trin

    def value_list(self):
        list = []
        for i in range(self.value):
            list.append(i+1)
        return list

    def afg(self):
        x = self.value_list() * ARVALUE
        return  x

def introspection_info(obj):
    info = {}
    type_1 = type(obj)
    info['type'] = type_1.__name__
    atrib = list(type_1.__dict__)
    list_atrib= []
    list_methods = []
    for i in atrib:
        if '__'  in i :
            list_methods.append(i)
        else:
            list_atrib.append(i)
    mod = getmodule(obj)
    info['attributes'] = list_atrib
    info['methods'] = list_methods
    info['module'] = mod


    return info

number_info = introspection_info(Dual('werden', 123, 'login'))
print(number_info)