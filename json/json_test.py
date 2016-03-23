#! -*- coding:utf8 -*-
import json


data = [ { 'a':'1', 'b':(2, 3), 'c':4.0 } ]
print 'DATA                        :', repr(data)
print 'dumps(data)                 :', json.dumps(data)
print 'dumps(data, sort_keys=True) :', json.dumps(data, sort_keys=True)
print 'dumps(data, indent=1)       :', json.dumps(data, indent=2)
print 'dumps(data, separators)     :', json.dumps(data, separators=(',',':'))

dict = {"a":"啊啊", "b":"啵啵", "c":"催催"}
print 'DATA                        :', repr(dict)
print 'dumps(dict)                 :', json.dumps(dict, encoding="UTF-8", ensure_ascii=False)