# -*- coding: utf-8-

from cffi import FFI
import os

def test_verify():
    ffi = FFI()
    header = open("foo.h").read() # 头文件和源文件最好都写在c里,确保编译通过,也方便调试
    ffi.cdef(header)
    source = open("foo.c").read()
    lib_dir = os.path.abspath(".") # 这个是必须的,不然编译时会找不到
    lib = ffi.verify(source, include_dirs=[lib_dir])
    print lib.test().a # 返回的是结构体, 这样的话就可以返回多个值了
    print lib.test().b

if __name__ == '__main__':
    test_verify()
