#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Python lists
 * @p: object
 *
 * Return: 0
 */

void print_python_list_info(PyObject *p)
{
	long int size_of_list, x, y;

	y = 0;
	PyObject *obj;

	size_of_list = PyList_Size(p);
	x = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size_of_list);
	printf("[*] Allocated = %ld\n", x);
	while (y < size_of_list)
	{
		obj = PyList_GetItem(p, y);
		printf("Element %ld: %s\n", y, Py_TYPE(obj)->tp_name);
		y++;
	}
}
