


import unittest
import os

from notebook_import import find_notebook, convert_to_module


class TestFindNotebook(unittest.TestCase):

    def test_PathDoesNotExist(self):
        self.assertRaises(FileNotFoundError, find_notebook, "nonexistent_sjwof3ewofeibfdnsib")


    def test_samedir(self):
        assert find_notebook(os.path.join('nested', 'directory', 'nested_example')) == "nested\\directory\\nested_example.ipynb", f"Error when calling as full path"
        assert find_notebook(os.path.join('nested', 'directory', 'nested_example.ipynb')) == "nested\\directory\\nested_example.ipynb", f"Error when calling as full path and .ipynb"
        assert find_notebook('nested_example', path=os.path.join('nested', 'directory')) == "nested\\directory\\nested_example.ipynb", f"Error when calling with separate path"
        assert find_notebook('nested_example.ipynb', path=os.path.join('nested', 'directory')) == "nested\\directory\\nested_example.ipynb", f"Error when calling with separate path and .ipynb"

    def test_nested(self):
        assert find_notebook(os.path.join('nested', 'directory', 'nested_example')) == "nested\\directory\\nested_example.ipynb", f"Error when calling as full path"
        assert find_notebook(os.path.join('nested', 'directory', 'nested_example.ipynb')) == "nested\\directory\\nested_example.ipynb", f"Error when calling as full path and .ipynb"
        assert find_notebook('nested_example', path=os.path.join('nested', 'directory')) == "nested\\directory\\nested_example.ipynb", f"Error when calling with separate path"
        assert find_notebook('nested_example.ipynb', path=os.path.join('nested', 'directory')) == "nested\\directory\\nested_example.ipynb", f"Error when calling with separate path and .ipynb"

    def test_preserveSpacingNested(self):
        assert find_notebook(os.path.join('nested', 'directory with space', 'nested_example')) == "nested\\directory with space\\nested_example.ipynb", f"Error when calling as full path"
        assert find_notebook(os.path.join('nested', 'directory with space', 'nested_example.ipynb')) == "nested\\directory with space\\nested_example.ipynb", f"Error when calling as full path and .ipynb"
        assert find_notebook('nested_example', path=os.path.join('nested', 'directory with space')) == "nested\\directory with space\\nested_example.ipynb", f"Error when calling with separate path"
        assert find_notebook('nested_example.ipynb', path=os.path.join('nested', 'directory with space')) == "nested\\directory with space\\nested_example.ipynb", f"Error when calling with separate path and .ipynb"

# class TestNotebookImport(unittest.TestCase):
#     # follow https://docs.python.org/3/library/unittest.html


#     def test_altImportMethods(self):
#         mymodule = import_notebook("example")
#         mymodule = import_notebook("example.ipynb")



#     def test_samelevel_class(self):
#         mymodule = import_notebook("example")
#         f = mymodule.Foo()
#         f.get_value()
#         assert f.get_value() == 'baz', f"function output different than expected, Expected 'baz', got Foo.get_value()={f.get_value()}"


#     def test_samelevel_function(self):
#         mymodule = import_notebook("example")
#         f = mymodule.Foo()
#         a,b,c = [1,2,3]
#         mymodule.testfunction(a,b,c)
#         assert mymodule.testfunction(a,b,c) == str(a)+ str(b)+ str(c), f"function output is different than expected\nExpected {str(a)+ str(b)+ str(c)}, got {mymodule.testfunction(a,b,c)}, check function definition in notebook"

#     def test_nested(self):
#         pass


class TestConvertNotebookToModule(unittest.TestCase):


    def test_notebookNameContainsSpace(self):
        self.assertRaises(ValueError, convert_to_module, "filename with space", overwrite=True)


    def test_curdiroverwrite(self):
        if os.path.exists("example.py"):
            os.remove("example.py")

        convert_to_module("example", overwrite=False)
        self.assertRaises(ValueError, convert_to_module, "example", overwrite=False)
        convert_to_module("example", overwrite=True)

    def test_nested(self):
        if os.path.exists("example.py"):
            os.remove("example.py")

        convert_to_module("example", overwrite=False)
        self.assertRaises(ValueError, convert_to_module, "example", overwrite=False)
        convert_to_module("example", overwrite=True)




if __name__ == '__main__':
    unittest.main()
