import json
import ujson

def monkey_patch():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps

monkey_patch()
print "in main.py json_name is", json.__name__


import sub
