

# Notebook prototyping

This repo makes prototyping via notebooks easier, by providing a way to strip them of experimental function calls.
In this manner, jupyter notebooks can be used to write, check, experiment, etc. with code while writing it while taking away the hassle of pasting all definitions into a new file.

With this you can:
- import notebooks directly
- strip notebooks to their bare class and function definitions.


# Usage

### importing the entire notebook contents

While developing it might be useful to import notebooks contents into other notebooks. This can be done via a pseudo import. currently the check for recursion is based on a heuristic trace stack depth

Running this makes objects that would be created in the secondary notebook available in a new notebook or script, but it should be noted that these exist *in a separate process*. as such it is strongly recommended to use convert_to_module + a normal import statement wherever possible instead
```
from notebook_import import import_notebook
import os

te = import_notebook('third_example', path=os.path.join('nested', 'directory'))
# alt import calls
# te = import_notebook('third_example.ipynb', path=os.path.join('nested', 'directory'))
# te = import_notebook(os.path.join('nested', 'directory', 'third_example'))
# te = import_notebook('nested.directory.third_example.ipynb')


te.foobar()
```


### conversion to .py files

It is recommended to do the conversion on a per-notebook basis

- Using the notebook name:
```
from notebook_import import convert_to_module
convert_to_module("example", overwrite=True)
```
- importing different notebooks contents cleanly, without their instantiated objects:
```
from notebook_import import convert_to_module
convert_to_module("second_example", overwrite=True)
import second_example as se
print(se.bar())
```
- Like importing notebooks, converting can also be done with notebooks in nested directories:
```
from notebook_import import convert_to_module
convert_to_module("third_example", overwrite=True, path=os.path.join("nested", "directory"))
import nested.directory.third_example as te
te.foobar()
```
- If you just to copy/paste something at the end of the notebook to convert them if they sucesfully finish running this can be done by also using ipynb([using ipynbname](https://pypi.org/project/ipynbname/)):
```
from notebook_import import convert_to_module
import ipynbname
nb_fname = ipynbname.name()
convert_to_module(nb_fname, True)
```

# Todos

- Currently the check for recursion is based on a heuristic trace stack depth, find a better way
- Make it a [pypi package](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
