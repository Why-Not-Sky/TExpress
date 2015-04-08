# -*- coding: utf8 -*-
msg = u'今天天氣真好'
encoded = msg.encode('utf8')
print repr(encoded)

encoded = '\xe4\xbb\x8a\xe5\xa4\xa9\xe5\xa4\xa9\xe6\xb0\xa3\xe7\x9c\x9f\xe5\xa5\xbd'
msg = encoded.decode('utf8')
print msg

class Demo:
    def __init__(self, i):
        self.i = i
        self.x = "xxx"
        self.y = "yyy"
        self.z = "zzz"

    def __str__(self):
        return str(self.i)

    def hello(self):
        print("hello " + self.__str__())

class SubDemo(Demo):
    pass

print(repr(0))
print(repr(0.0))
print(repr(0j))
print(repr("0"))
print(repr([0]))
print(repr((0,)))
print(repr({0}))
print(repr(Demo(22)))
print(repr(SubDemo))