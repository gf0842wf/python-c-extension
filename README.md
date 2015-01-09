### c扩展python,提升性能 ###

- ctypes  
完全是c写的,目前linux的.so测试ok了, windows的.dll没有测试好
- c写python扩展(示例见之前xorcrypt模块: https://github.com/gf0842wf/ggame/tree/master/xorcrypt)  
写法很不爽,可以安装模块
- cython  
基本是python写法,很好用,性能较低
- cffi  
可以直接嵌入c代码,不过修改代码后要删除目录下的`__pycache__`目录

`测试性能: cffi≈ctypes≈c写python扩展>cython>原生python`
