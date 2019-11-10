#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'class Student'
__author__ = 'denglz'

class Student(object):
#    def __init__(self, score):
#        self.__name  = name

#    def print_score(self):
#        print ('%s : %s ' % (self.__name, self.__score))
    
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be int')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100 ')
        self.__score = value


s = Student()
s.score = 99
print(s.score)
