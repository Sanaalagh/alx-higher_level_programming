#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t length = PyUnicode_GET_LENGTH(p);
    const char *value = PyUnicode_AsUTF8(p);

    fprintf(stderr, "[.] string object info\n");
    fprintf(stderr, "  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
    fprintf(stderr, "  length: %zd\n", length);
    fprintf(stderr, "  value: %s\n", value);
}
