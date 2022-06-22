import json

version = "0.01"

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
        # you can specify save=False
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
        {'name': 'Petya', 'lvl': '100',
        'subjects': {'monday': 'english', 'tuesday': 'physics'}}
        #
        # cancel
        #
        >>> file.add('name','Petya')
        >>> file.data
        {'name': 'Petya'}
        >>> file.cancel()
        >>> file.data
        {}
        #
        # multiples
        #
        >>> file.data
        {'age': 'seventeen'}
        >>> file.add_multiple(False, name='Vasya', lvl='four')
        >>> file.data
        {'age': 'seventeen', 'name': 'Vasya', 'lvl': 'four'}
        >>> file.delete_multiple(False, 'name', 'lvl')
        >>> file.data
        {'age': 'seventeen'}
        >>> file.cancel()
        >>> file.data
        {'age': 'seventeen', 'name': 'Vasya', 'lvl': 'four'}
        >>> file.change_multiple(name='Petya', lvl='five')
        >>> file.data

        #
        # save
        #
        # when you change JSON_manager any way it doesn't change json file
        # if file.auto_save = False
        >>> file.save()
        #
        New func!
        file.last_changes()# shows last acts
        '''
    print(info)


class JSON_manager():
    ''' enter help() to get more information '''
    
    def __init__(self,data={},name="",read=False,create=False,save=True,
                 original=True):
        self.data = data
        self.name = name
        self.original = original
        self.auto_save = False
        #last_change
        self.changes_list = []
        self.last_change = None
        self.data_dict = {}
        self.funcs = {
            self.add: self.delete_multiple,
            self.delete: self.add_multiple,
            self.change: self.change_multiple,
            None: None
            }
        self.funcs_repr = {
            self.add: 'add',
            self.delete: 'delete',
            self.change: 'change',
            self.add_multiple: 'add_multiple',
            self.delete_multiple: 'delete_multiple',
            self.change_multiple: 'change_multiple',
            None: None
            }
        
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
                
        self._update(None,{})
        self.changes_list.pop(0)

    def _update(self, name_func, data_dict):
        self.keys = list(self.data.keys())
        self.values = list(self.data.values())
        self.data_dict = data_dict
        self.last_change = self.funcs[name_func]
        last_change_repr = self.funcs_repr[name_func]
        self.changes_list.append( (last_change_repr, self.data_dict) )

        if self.auto_save: self.save()
        
    def change(self,key,value):
        if key not in self.keys: Error('this key doesn\'t exist'); return
        data_dict = {key: self.data[key]}
        self.data[key] = value
        self._update(self.change, data_dict)

    def change_multiple(self, stop=False, **kwargs):
        data_dict = {}
        for key,value in kwargs.items():
            if key in self.keys:
                self.data[key] = value
                data_dict[key] = value
            else:
                Error('this key doesn\'t exist')
                if stop: return
        self._update(self.change, data_dict)

    def add(self,key,value):
        if key in self.keys: Error('this key exists'); return
        data_dict = {key:value}
        self.data[key] = value
        self._update(self.add, data_dict)

    def add_multiple(self, stop=False, **kwargs):
        data_dict = {}
        for key,value in kwargs.items():
            if key not in self.keys:
                self.data[key] = value
                data_dict[key] = value
            else:
                Error('this key exists')
                if stop: return
        self._update(self.add, data_dict)

    def delete(self,key):
        if key not in self.keys: Error('this key doesn\'t exist'); return
        poped = self.data.pop(key)
        data_dict = {key: poped}
        self._update(self.delete, data_dict)

    def delete_multiple(self, stop=False, *args):
        ''' Always specify stop True or False to avoid losing first arg '''
        data_dict = {}

        for key in args:
            if key in self.keys:
                poped = self.data.pop(key)
                data_dict[key] = poped
            else:
                Error('this key doesn\'t exist')
                if stop: return
                
        self._update(self.delete, data_dict)

    def open_dict(self,key):
        '''
        returns opened dict as JSON_manager
        maybe bugs are exists please tell me about it
        '''
        if key not in self.keys: Error('this key doesn\'t exist'); return
        if isinstance(self.data.get(key), dict):
            try:
                return JSON_manager(self.data[key],original=False)
            except Exception as exc:
                Error(exc)

    def cancel(self):
        try:
            if self.last_change == self.delete_multiple:
                self.last_change( False, *self.data_dict )
            else:
                self.last_change( **self.data_dict )
        except Exception as exc:
            Error(exc)
    def last_changes(self):
        for i in self.changes_list:
            print(i)
        
    def save(self):
        if not self.original: return
        name = self.name if self.name == "" else 'unnamed.json'
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

    

