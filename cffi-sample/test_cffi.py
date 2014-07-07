# -*- coding: utf-8 -*-

from cffi import FFI
import time

ffi = FFI()
ffi.cdef("""     // some declarations from the man page
	unsigned long long acc();
""")
lib = ffi.verify("""   // passed to the real C compiler
unsigned long long acc()
{
	unsigned long long  i = 0;
	unsigned long long  s = 0;
	for(i=0; i<100000000; i++)
	{
		s += i;
	}
	return s;
}
""")   # or a list of libraries to link with
t0 = time.time()
print lib.acc()
print time.time() - t0
# print ffi.string(s) # 这个针对char* 的变量
