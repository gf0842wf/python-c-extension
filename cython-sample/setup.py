# -*- coding: utf-8 -*-

"""会自动生成hello.c文件"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
 
setup(
  name = 'hello',
  ext_modules=cythonize([
    Extension("hello", ["hello.pyx"]),
    ]),
)
 