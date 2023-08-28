#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Gives data of the PyFloatObject.
 * @p: The PyObject
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

/* Check if the PyObject is a valid PyFloatObject */
	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

/* Extract the float value from the PyFloatObject */
	value = ((PyFloatObject *)p)->ob_fval;

/* Convert the float value to a string */
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

/* Print the float value as a string */
	printf("  value: %s\n", string);
	}

/**
 * print_python_bytes - Gives data of the PyBytesObject.
 * @p: The PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

/* Check if the PyObject is a valid PyBytesObject */
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

/* Get the size of the bytes object */
	size = PyBytes_Size(p);

/* Print the size of the bytes object */
	printf("  size: %zd\n", size);

/* Access the raw byte data of the PyBytesObject */
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));

/* Print the string representation of the bytes object */
	printf("  trying string: %s\n", string);

/* Print the first few bytes of the bytes object */
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

/**
 * print_python_list - Gives data of the PyListObject.
 * @p: The PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

/* Check if the PyObject is a valid PyListObject */
	if (PyList_CheckExact(p))
	{
/* Get the size of the list */
	size = PyList_GET_SIZE(p);

/* Print the size of the Python List */
	printf("[*] Size of the Python List = %zd\n", size);

/* Print the allocated memory for the list */
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

/* Iterate through the elements of the list */
	while (i < size)
	{
/* Get an item from the list */
		item = PyList_GET_ITEM(p, i);
/* Print the element number and its type name */
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

/* Check if the item is a bytes object */
	if (PyBytes_Check(item))
	print_python_bytes(item);
/* Print information about the bytes object */

/* Check if the item is a float object */
	else if (PyFloat_Check(item))
	print_python_float(item);
/* Print information about the float object */
	i++;
/* Move to the next element */
	}
	}
	else
	{
	printf("  [ERROR] Invalid List Object\n");
	}
}
