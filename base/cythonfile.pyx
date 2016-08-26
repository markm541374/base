# setuptools: language = c++
from libcpp.vector cimport vector
import numpy as np

def cyfunc():
    cdef vector[int] b = [1,2,3]
    print b
    cdef int a = 4242
    return  "I'm a cython function {}".format(a)