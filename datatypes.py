s = "hello"
print(type(s))#str
s = 1
print(type(s))#int
s = 1.5
print(type(s))#float
s = 1+1J
print(type(s))#comlex
s = True
print(type(s))#bool
s = None
print(type(s))#None
s = [1,2]
print(type(s))#list
s = (1,2)
print(type(s))#tuple
s = {1,2}
print(type(s))#set
s = {1:"1",2:"2"}
print(type(s))#dict
s = frozenset({1,2})
print(type(s))#frozenset
s = b"hello"
print(type(s))#byte
s=range(6)
print(type(s))#range
s=bytearray(5)
print(type(s))#bytearray
s= memoryview(bytes(5))
print(s)#memoryview
