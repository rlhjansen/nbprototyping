

# Notebook prototyping

This repo makes prototyping via notebooks easier, by providing a way to strip them of experimental/veryfying function calls only retaining function/class definitions and imports.
In this manner, jupyter notebooks can be used to write, check, experiment, etc. with code while writing it while taking away the hassle of pasting all definitions into a new file.

With this you can:
- strip notebooks to their bare class/function definitions & imports.


# Usage

To install:

```
pip install notebook-prototyping
```

Then to convert the currently active notebook to a python file:

```
import ipynbname
nb_fname = ipynbname.name()
convert_to_module(nb_fname, overwrite=True)
```

You can also convert different notebooks form within a notebook or python file

```
convert_to_module("path/to/my/notebook_file", overwrite=True)
```

However, especially with overwrite=True this might be ill-advised, overwrite is set to False by default



# Todos

- [add classifiers](https://pypi.org/classifiers/)
- add functionality to run tests before conversion
