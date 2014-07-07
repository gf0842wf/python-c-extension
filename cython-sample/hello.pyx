cdef extern from"stdio.h":
    extern int printf(const char *format, ...) # 使用这种方式导入c库函数
    
def acc():
    i, s = 0, 0
    while i < 100000000:
        s += i
        i += 1
    return s