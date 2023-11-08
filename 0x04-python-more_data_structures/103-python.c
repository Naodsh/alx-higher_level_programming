#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - prints info about the Python list, including its size
 *
 * @p:  A pointer to a PyObject representing a Python list.
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	int i, size;

	size = PyList_Size(p);
	PyListObject *list = (PyListObject *)p;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GET_ITEM(p, i);

		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints info about the Python bytes object
 *
 * @p:  A pointer to a PyObject representing a Python bytes object.
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int i, size;

	size = PyBytes_Size(p);

	PyBytesObject *bytes = (PyBytesObject *)p;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
		return;
	}

	if (size > 10)
		size = 10;

	printf(
	"[.] bytes object info\n size: %d\n trying string: %s\n first %d bytes:"
			, size, PyUnicode_AsUTF8(PyObject_Repr(p)), size);

	for (i = 0; i < size; i++)
	{
		printf(" %02x", (unsigned char)bytes->ob_sval[i]);
	}

	printf("\n");
}
