import json

def Error(ad_info=""):
    print(f'something is going wrong... {ad_info}')

class JSON_object():
    '''
    common functions for management json files
    add,delete,change,save
    '''
    def __init__(self,data,name):
        self.data = data
        self.name = name
        self._update()

    def _update(self):#kind of low level func :D
        self.keys = list(self.data.keys())
        self.values = list(self.data.values())
        
    def change(self,key,value):
        if key in self.keys:
            self.data[key] = value
            self._update()
        else: Error('this key doesn\'t exists')

    def add(self,key,value):
        if key not in self.keys:
            self.data[key] = value
            self._update()
        else: Error('this key exists')

    def delete(self,key):
        if key in self.keys:
            self.data.pop(key)
            self._update()
        else: Error('this key exists')
        
    def save(self):
        with open(self.name, "w") as write_file:
            json.dump(self.data, write_file)


def read(name):
    '''
    reads JSON file and returns it as class JSON_object
    Vasya = read('vasya.json')
    '''

    def reading(name):
        with open(name,'r') as read_file:
            data = JSON_object( json.load(read_file), name )
        return data
    
    
    try:
        return reading(name)
    except Exception as exc:
        Error(exc)

def create(name,_data={},debug=False):
    '''
    creates JSON file and returns it as class JSON_object
    Vasya = create('vasya.json')
    '''
    data = _data
    def creating(name,data):
        with open(name,'w') as write_file:
            json.dump(data, write_file)
        data = JSON_object( data, name )
        return data
    
    try:
        return creating(name,data)
    except Exception as exc:
        Error(exc)

