#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - Prints list info
 * @p: Python Object
 *
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int size, x;
	PyListObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		obj = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
} 

/**
 * print_python_bytes - prints basic information on python bytes
 * @p: Python Object
 *
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *letter;
	long int size, x, cap;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	letter = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", letter);

	if (size >= 10)
		cap = 10;
	else
		cap = size + 1;

	printf("  first %ld bytes:", cap);

	for (x = 0; x < cap; x++)
		if (letter[x] >= 0)
			printf(" %02x", letter[x]);
		else
			printf(" %02x", 256 + letter[x]);

	printf("\n");
}
