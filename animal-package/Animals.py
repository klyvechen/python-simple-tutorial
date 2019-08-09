# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 8:04:19 2019

@author: klyve
"""

class Cat:
    __numberOfCats = 0 #類別屬性
    
    def __init__(self, name, gender):
        self.name = name ##物件屬性
        self.gneder = gender
        self.__age = 3 ##私有物件屬性
        Cat.__numberOfCats += 1 ##操作類別屬性

    def bark(self):
        print "bark"
    
    def sayHello(self):
        print "Hi, Im a " + Cat.__name__ + " my name is " + self.name
        
    def numberOfMembers(self):
        print "Hi, Im a " + Cat.__name__ + " there are " + Cat.__numberOfCats + "in the group!"
        
        
class Dog:
    numberOfDogs = 0
    def __init__(self, name, gender):
        self.name = name
        self.gneder = gender
        

    def bark(self):
        print "bark4"
    
    def sayHello(self):
        print "Hi my name is " + self.name
        
##五個內建python函數
print Cat.__doc__    #Class documentation string or none, if undefined.
print Cat.__dict__   #Dictionary containing the class's namespace.
print Cat.__name__   #Class name
print Cat.__module__ #Module name in which the class is defined. This attribute is "__main__" in interactive mode.
print Cat.__bases__  #A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.


