# [Liao Xuefeng's Blog](http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431608990315a01b575e2ab041168ff0df194698afac000) reading notes

### python brief

python good at
- web service, backend service
- tools
- glue of other codes

python cons
- slow
- code no encrpytion

### install python & python intepreter typs

- brew, virtualenv, conda?
- CPython, IPython, Jython, IronPython, PyPy

### data types & var

- True, and, None
```python
a = 'ABC'
b = a
a = 'XYZ'
print(b)
>>> ABC

9/3
>>> 3.0

10//3
>>> 3
```
### string encoding

- ASCII (1 byte) 127char
- Unicode
   1. UTF-8 (1-6 bytes) compatible with ACSII
   2. UTF-16

*commonly the RAM and network use Unicode*

![local model](http://www.liaoxuefeng.com/files/attachments/001387245992536e2ba28125cf04f5c8985dbc94a02245e000/0)
![network model](http://www.liaoxuefeng.com/files/attachments/001387245979827634fd6204f9346a1ae6358d9ed051666000/0)

python3 use Unicode encoding in RAM
```python
>>> '\u4e2d\u6587'
'中文'

>>> ord('A')
65
>>> ord('中')
20013
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

when use in Disk or Network should use bytes
```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87' 

>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

### changable type and not changable type
## Notice: str is not changable

- not changable: str, tuple
- changable: list
```python
s = 'abc'
s.replace('a', 'A')
s = 'abc'
```

### [string](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) & format output

```python
str.capitalize()  str.center(width[, fillchar])  str.count(sub[, start[, end]])
str.encode(encoding='utf-8', error='strict')  
str.startwiths(prefix[, start[, end]])  str.endswith(suffix[, start[, end]])
str.expandtabs(tabsize=8) Return a copy of the string where all tab characters are replaced by one or more spaces
str.find(sub[, start[, end]]) if not exist return -1, no need index use sub in str
str.format(*args, **kwargs) >>> "The sum of 1 + 2 is {0}".format(1+2)
str.format_map(mapping) >>> '{name} was born in {country}'.format_map(Default(name='Guido'))
str.index(sub[, start[, end]])

str.isalnum()  str.isalpha()  str.isdecimal()  str.isdigit()  str.islower()
str.isnumeric() str.printable()  str.isspace()  str.isupper()

str.zfill(width)
>>> "42".zfill(5)
'00042'
>>> "-42".zfill(5)
'-0042'

str.translate(table)
Return a copy of the string in which each character has been mapped through the given translation table. 

str.join(iterable)  str.ljust(width[, fillchar])  
str.lower()  str.upper()
str.lstrip([chars])  str.replace(old, new[, count])  
>>> 'www.example.com'.lstrip('cmowz.')
'example.com'
str.strip([chars])

str.swapcase()
str.title()
>>> "they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"
>>> import re
>>> def titlecase(s):
...     return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                   lambda mo: mo.group(0)[0].upper() +
...                              mo.group(0)[1:].lower(),
...                   s)
...
>>> titlecase("they're bill's friends.")
"They're Bill's Friends."

str.split(sep=None, maxsplit=-1)
Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
str.splitlines()
>>> "One line\n".splitilnes()
['One line']
>>> "One line\n".split('\n')
['One line', '']

str.partition(sep)
Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator. If the separator is not found, return a 3-tuple containing the string itself, followed by two empty strings.

str.rfind   str.rindex  str.rjust  str.rpartation  str.rsplit  str.rstrip


>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'

>>> '%2d-%03d' % (3, 1)
' 3-001'
>>> '%.2f' % 3.1415926
'3.14'

>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
```
#### list & turple

```python
list.append  list.count   list.insert  list.reverse
                list.clear   list.extend  list.pop     list.sort
                                list.copy    list.index   list.remove

 tuple.count
                  tuple.index
```

### for & while & break & continue

### [dict & set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)

```python
dict.clear      dict.get        dict.pop        dict.update
                dict.copy       dict.items      dict.popitem    dict.values
                                dict.fromkeys   dict.keys       dict.setdefault
d = {'annie':1, 'jack':2}
if 'jony' in d:
    print(d['jony'])

d.get['jony']
>>> None
d.get['jony', 'Not exist']
>>> Not exit

setdefault(key[, default])
If key is in the dictionary, return its value. If not, insert key with a value of default and return default. default defaults to None.

update([other])
Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None.

update() accepts either another dictionary object or an iterable of key/value pairs (as tuples or other iterables of length two). If keyword arguments are specified, the dictionary is then updated with those key/value pairs: d.update(red=1, blue=2).
-----------------------------

len(s), x in s, x not in s, isdisjoint(other), issubset(other),
set <= other, 
union(*others), set | other1 | other2 |...
intersection(*others), set & other1 & other2 & ...
difference(*others), set - other1 - other2 - ...
dd(elem)
Add element elem to the set.

remove(elem)
Remove element elem from the set. Raises KeyError if elem is not contained in the set.

discard(elem)
Remove element elem from the set if it is present.

pop()
Remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

update(*others)
set |= other | ...
Update the set, adding elements from all others.
```
