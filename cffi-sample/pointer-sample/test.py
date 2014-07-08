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
    varsp = ffi.new("foo_s*")
    print varsp[0].a, varsp[0].b
    lib.test(varsp)
    print varsp[0].a, varsp[0].b

if __name__ == '__main__':
    test_verify()
