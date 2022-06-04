import json

def Error(ad_info=""):
    print(f'something is going wrong... {ad_info}')
    
def help():
    info = '''
        JSON_manager allows you manage json files
        file = JSON_manager()#here you have empty object
        but you already can work with json   
        
        if you want read file
        => file.read("name.json")
        or during creation set read=True and set name
        if you want create file
        => file.create("name.json")
        or during creation set create=True and set name
        also if you don't want create json file at this moment
        you can set save=False
        '''
    print(info)

class JSON_manager():
    ''' enter help() to get more information '''
    
    def __init__(self,data={},name="",read=False,create=False,save=True):
        self.data = data
        self.name = name
        
        if read:
            try:
                self.read(name)
            except Exception as exc:
                Error(exc)

        if create:
            try:
                self.create(name,self.data,save)
            except Exception as exc:
                Error(exc)
                
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
        name = self.name
        if name == "": name = 'unnamed.json'
        try:
            with open(name, "w") as write_file:
                json.dump(self.data, write_file)
        except Exception as exc:
            Error(exc)
            
    def read(self,name):
        '''
        makes this object a representation of your json file
        '''
        try:
            with open(name,'r') as read_file:
                self.data = json.load(read_file)
                self.name = name
        except Exception as exc:
            Error(exc)

    def create(self,name,data,save=True):
        '''
        creates JSON file
        and makes this object a representation of it
        '''
        try:
            self.data = _data
            self.name = name
            if save: self.save()
        except Exception as exc:
            Error(exc)

    
