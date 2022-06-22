json-management
===============

Hi! This is my first project on github and maybe it is not very usefull, i just want to increase my lvl and maybe meet some criticism! Also i want to work at IT but now i am hihgschool student.

json data manager 

you have object and you can edit it as you need and save when you need

JSON_manager allows you manage json files

.. code-block:: python

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
    
