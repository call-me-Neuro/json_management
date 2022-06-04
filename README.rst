# json-management
json data manager 

it works like in django:

you have object and you can edit it as you need and save when you need

JSON_manager allows you manage json files

.. code-block:: python

    >>> file = JSON_manager()#here you have empty object

but you already can work with json   

if you want open file

.. code-block:: python

    >>> file.read("name.json")

or during creation set read=True and set name

if you want create file

.. code-block:: python

    >>> file.create("name.json")

or during creation set create=True and set name

also if you don't want create json file at this moment

you can set save=False

