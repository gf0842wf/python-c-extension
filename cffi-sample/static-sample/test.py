# -*- coding: utf-8-

from cffi import FFI
import os

def test_verify():
    ffi = FFI()
    header = open("foo.h").read()
    ffi.cdef(header)
    source = open("foo.c").read()
    lib_dir = os.path.abspath(".")
    lib = ffi.verify(source, include_dirs=[lib_dir])
    print lib.test()
	# result: 1
    print lib.test()
	# result: 2
	# 哈哈, python没有static变量, c有, 这里可以在python里用c的

if __name__ == '__main__':
    test_verify()
