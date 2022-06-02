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
        if key not in self.keys: Error('this key doesn\'t exist'); return
        self.data[key] = value
        self._update()

    def add(self,key,value):
        if key in self.keys: Error('this key exists'); return
        self.data[key] = value
        self._update()

    def delete(self,key):
        if key not in self.keys: Error('this key doesn\'t exist'); return
        self.data.pop(key)
        self._update()
        
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

def create(name,_data={},debug=False,save=True):
    '''
    creates JSON file and returns it as class JSON_object
    Vasya = create('vasya.json')
    '''
    data = _data
    def creating(name, data, save):
        data = JSON_object( data, name )
        if save:
            data.save()
        return data
    
    try:
        return creating(name, data, save)
    except Exception as exc:
        Error(exc)

