


import unittest
import os

from notebook_import import find_notebook, import_notebook, convert_module


class TestFindNotebook(unittest.TestCase):

    def test_PathDoesNotExist(self):
        self.assertRaises(FileNotFoundError, find_notebook, "nonexistent_sjwof3ewofeibfdnsib")


    def test_samedir(self):
        assert find_notebook(os.path.join('nested', 'directory', 'third_example')) == "nested\\directory\\third_example.ipynb", f"Error when calling as full path"
        assert find_notebook(os.path.join('nested', 'directory', 'third_example.ipynb')) == "nested\\directory\\third_example.ipynb", f"Error when calling as full path and .ipynb"
        assert find_notebook('third_example', path=os.path.join('nested', 'directory')) == "nested\\directory\\third_example.ipynb", f"Error when calling with separate path"
        assert find_notebook('third_example.ipynb', path=os.path.join('nested', 'directory')) == "nested\\directory\\third_example.ipynb", f"Error when calling with separate path and .ipynb"

    def test_nested(self):
        assert find_notebook(os.path.join('nested', 'directory', 'third_example')) == "nested\\directory\\third_example.ipynb", f"Error when calling as full path"
        assert find_notebook(os.path.join('nested', 'directory', 'third_example.ipynb')) == "nested\\directory\\third_example.ipynb", f"Error when calling as full path and .ipynb"
        assert find_notebook('third_example', path=os.path.join('nested', 'directory')) == "nested\\directory\\third_example.ipynb", f"Error when calling with separate path"
        assert find_notebook('third_example.ipynb', path=os.path.join('nested', 'directory')) == "nested\\directory\\third_example.ipynb", f"Error when calling with separate path and .ipynb"

class TestNotebookImport(unittest.TestCase):
    # follow https://docs.python.org/3/library/unittest.html

    def test_upper(self):
        pass

    def test_isupper(self):
        pass

    def test_split(self):
        pass


class TestConvertNotebookToModule(unittest.TestCase):


    def test_notebookNameContainsSpace(self):
        with self.assertRaises as context:
            convertModule("filename with space")
        self.assertTrue('containing a space character' in context.exception)

    def test_curdir(self):
        # convert_module
        pass

    def test_nested(self):
        # should preserve spacing in leading directories but raise an error if paces are in a notebook filename
        pass

    def test_overwrite(self):
        if os.path.exists("example.py"):
            os.remove("example.py")

        convert_to_module("example", overwrite=False)
        self.assertRaises(ValueError, convert_to_module, "example", overwrite=False)
        self.assertDoesNotRaise(ValueError, convert_to_module, "example", overwrite=True)


if __name__ == '__main__':
    unittest.main()
