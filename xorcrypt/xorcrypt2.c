#include <Python.h>
#include <stdio.h>

static PyObject* xor_crypt(PyObject* self, PyObject* args)
{
    char* s;
    unsigned int key = 0;
    unsigned int M1 = 0;
    unsigned int IA1 = 0;
    unsigned int IC1 = 0;
    unsigned int size;
    
    PyObject* v;
    char *p;
    unsigned int i = 0;
    unsigned char c;
    
    // 解析参数 s#表示字符串和它的长度, |后的表示可选参数, I是unsigned
    if(!PyArg_ParseTuple(args, "s#|IIII", &s, &size, &key, &M1, &IA1, &IC1))
        return NULL;
    
    if(key == 0)
        key = 1;
    if(M1 == 0)
        M1 = 1 << 19;
    if(IA1 == 0)
        IA1 = 2 << 20;
    if(IC1 == 0)
        IC1 = 3<< 21;
    
    // v是python的空字符串, 长度为size
    v = PyString_FromStringAndSize((char*)NULL, size);
    if(v == NULL)
        return NULL;
    
    // p是把python的字符串v转换为c的字符串, 对p进行操作也会影响v
    p = PyString_AS_STRING(v);
    for (i = 0; i < size; i++) {
        c = (unsigned char)s[i];
        key = IA1 * (key % M1) + IC1;
        *p = c ^ (unsigned char)((key >> 20)&0xff);
            p++;
	}
    return v;
}

static PyMethodDef xorcrypt2_methods[] = {
    {"crypt", (PyCFunction)xor_crypt,  METH_VARARGS,
    PyDoc_STR("encrypt/decrypt(string) -> generate the string.")},

    {NULL, NULL}  // sentinel
};

PyDoc_STRVAR(module_doc, "XOR encrypt/decrypt module.");

/* Initialization function for the module (be called when init) */
PyMODINIT_FUNC initxorcrypt2(void)
{
    PyObject *m;

    m = Py_InitModule3("xorcrypt2", xorcrypt2_methods, module_doc);

    if (m == NULL)
        return;

    PyModule_AddStringConstant(m, "__version__", "0.2");
}