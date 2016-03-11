#include <Python.h>

static PyObject *
divide(PyObject *self, PyObject *args)
{
    double x;
    double y;
    double sts;

    if (!PyArg_ParseTuple(args, "dd", &x, &y))
        return NULL;
    sts = x/y;
    return Py_BuildValue("d", sts);
}

// Module's method table and initialization function
// See: http://docs.python.org/extending/extending.html#the-module-s-method-table-and-initialization-function
static PyMethodDef DivideMethods[] = {
    {"divide", divide, METH_VARARGS, "divide two numbers"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC // does the right thing on Windows, Linux, etc.
initdivide(void) {
    // Module's initialization function
    // Will be called again if you use Python's reload()

    Py_InitModule("divide", DivideMethods);
}
