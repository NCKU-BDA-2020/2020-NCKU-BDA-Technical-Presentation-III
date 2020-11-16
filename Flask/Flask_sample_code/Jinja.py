# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:50:51 2020

@author: hao05
"""

from jinja2 import Template


Template("{{ 10 // 3 }}").render()

Template("{{ var[1] }}").render(var=[1,2,3])

Template("{{ var['profession'] }}").render(var={'name':'tom', 'age': 25, 'profession': 'Manager' })

Template("{{ var[2] }}").render(var=("c", "c++", "python"))

double = lambda x : x*2
Template("{{ 2*double(2) }}").render(double=double)


class Foo:
    def  __str__(self):
        return "This is an instance of Foo class"


Template("{{ var }}").render(var=Foo())

class Foo:
     def __init__(self, i):
         self.i = i
     def do_something(self):
         return "do_something() called"

Template("{{ obj.i }}").render(obj=Foo(5))
Template("{{ obj.do_something() }}").render(obj=Foo(5))