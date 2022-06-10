json-management
===============

json data manager 

you have object and you can edit it as you need and save when you need

JSON_manager allows you manage json files

.. code-block:: python

    >>> file = JSON_manager()# here you have empty object
    # but you already can work with json   

    # if you want open file
    >>> file.read("name.json")
    # or
    >>> file = JSON_manager(name='name',read=True)
    # if you want create file
    >>> file.create()#here you can redefine name="name", data={...}
    #using self.name to create, default is "" and this way saves as "unnamed.json"
    # or
    >>> file = JSON_manager(name='name',create=True)
    # also if you don't want create json file at this moment
    # you can set save=False
    #
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
    >>> i = test.open_dict('subjects')#it is instance of JSON_manager class
    >>> i.data
    {'monday': 'math', 'tuesday': 'physics'}
    >>> i.change('monday','english')
    >>> i.data
    {'monday': 'english', 'tuesday': 'physics'}
    >>> test.data#changes from i copies in original
    {'name': 'Petya', 'lvl': '100', 'subjects': {'monday': 'english', 'tuesday': 'physics'}}
    #
    # save
    #
    # when you change JSON_manager any way it doesn't change json file
    >>> file.save()
    
