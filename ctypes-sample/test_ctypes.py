# -*- coding: utf-8 -*-

from ctypes import *
import time

libc = CDLL("./acc.so")
libc.acc.restype = c_ulonglong # ��Ҫ��ȷָ����������
# libc.say_hello.restype = c_char_p
t0 = time.time()
print libc.acc()
print time.time() - t0

t1 = time.time()
s = 0
for i in xrange(100000000):
	s += i
print s
print time.time() - t1
