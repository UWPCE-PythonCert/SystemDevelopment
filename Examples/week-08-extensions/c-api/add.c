#include <Python.h>

static PyObject *
add(PyObject *self, PyObject *args)
{
    int x;
    int y;
    int sts;

    if (!PyArg_ParseTuple(args, "ii", &x, &y))
        return NULL;
    sts = x+y;
    return Py_BuildValue("i", sts);
}

// Module's method table and initialization function
// see: https://docs.python.org/2/extending/extending.html#the-module-s-method-table-and-initialization-function
static PyMethodDef AddMethods[] = {
    {"add", add, METH_VARARGS, "add two numbers"},
    {NULL, NULL, 0, NULL} // sentinel
};


PyMODINIT_FUNC
initadd(void) {
    // Module's initialization function
    // Will be called again if you use Python's reload()
    (void) Py_InitModule("add", AddMethods);
}
