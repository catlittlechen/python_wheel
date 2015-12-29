# -*- coding:utf8 -*_
"""
弱引用
"""


import weakref


class Children(object):
    """children class"""
    def __init__(self, parent, name):
        self.name = name
        self.parent = parent
        print self.name + ": my parent is " + self.parent.name

    def set_parent(self, parent):
        """set parent"""
        self.parent = parent

    def get_parent(self):
        """get parent"""
        return self.parent


class Parent(object):
    """parent class"""
    def __init__(self, name):
        self.name = name
        self.children = None

    def add_children(self, name):
        """have a children"""
        self.children = Children(weakref.proxy(self), name)
        print self.name + ": my children is " + self.children.name

    def del_children(self):
        """lose a children"""
        self.children = None

if __name__ == "__main__":
    p = Parent("Jack")
    p.add_children("Salay")
