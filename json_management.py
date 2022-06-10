import json

def Error(ad_info=""):
    print(f'something is going wrong... {ad_info}')
    
def help():
    info = '''
        JSON_manager allows you manage json files
        file = JSON_manager()# here you have empty object
        # but you already can work with json   
        
        # if you want open file
        >>> file.read("name.json")
        # or
        >>> file = JSON_manager(name='name',read=True)
        # if you want create file
        >>> file.create()
        # or
        >>> file = JSON_manager(name='name',create=True)
        # also if you don't want create json file at this moment
        # you can set save=False
        >>> test = JSON_manager(name='test.json',read=True)
        >>> test.data
        {'name': 'Petya', 'lvl': '100'}
        #
        # change
        #
        >>> test.change('name','Vasya')
        >>> test.data
        {'name': 'Vasya', 'lvl': '100'}
        #
        # add
        #
        >>> test.add('language','Pyton')
        >>> test.data
        {'name': 'Vasya', 'lvl': '100', 'language': 'Python'}
        #
        # delete
        #
        >>> test.delete('language')
        >>> test.data
        {'name': 'Vasya', 'lvl': '100'}
        #
        # open_dict
        #
        >>> test = JSON_manager(name='test.json',read=True)
        >>> test.data
        {'name': 'Petya', 'lvl': '100',
        'subjects': {'monday': 'math', 'tuesday': 'physics'}}
        >>> i = test.open_dict('subjects')
        # it is instance of JSON_manager class
        >>> i.data
        {'monday': 'math', 'tuesday': 'physics'}
        >>> i.change('monday','english')
        >>> i.data
        {'monday': 'english', 'tuesday': 'physics'}
        >>> test.data
        # changes from i copies in original
        {'name': 'Petya', 'lvl': '100', 'subjects': {'monday': 'english', 'tuesday': 'physics'}}
        #
        # save
        #
        # when you change JSON_manager any way it doesn't change json file
        >>> file.save()
        '''
    print(info)
    

class JSON_manager():
    ''' enter help() to get more information '''
    
    def __init__(self,data={},name="",read=False,create=False,save=True,
                 original=True):
        self.data = data
        self.name = name
        self.original = original
        
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

    def open_dict(self,key):
        '''
        returns opened dict as JSON_manager
        maybe bugs are exists please tell me about it
        '''
        if key not in self.keys: Error('this key doesn\'t exist'); return
        if type( self.data.get(key) ) == dict:
            try:
                return JSON_manager(self.data[key],original=False)
            except Exception as exc:
                Error(exc)
        
    def save(self):
        if not original: return
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

    def create(self,name="",data={},save=True):
        '''
        creates JSON file
        and makes this object a representation of it
        '''
        try:
            if data != {}: self.data = data
            if name != "": self.name = name
            if save: self.save()
        except Exception as exc:
            Error(exc)

    
