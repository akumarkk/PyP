###### mutable and immutable
what couldbne  changed in memory 

mutable- sets
immurable - primitive types like int etc

```
>>> var==2
True
>>> id(2)
140734655121880
>>> id(12)
140734655122200
>>>
>>>
>>>
>>> var = 12
>>> id(12)
140734655122200
>>> id(1299)
2266499350064
>>>
>>>
>>> s = set()
>>> id(s)
2266500003904
>>> s.add("plants")
>>> s.add("anim")
>>>
>>>
>>> id(s)
2266500003904
>>>


```