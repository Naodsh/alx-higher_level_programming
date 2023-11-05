#include "lists.h"
/**
 * print_python_list_info - Prints information about a Python list.
 * @p: Python list object
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = Py_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
