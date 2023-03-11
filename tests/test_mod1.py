# Can be called directly from Intellij
# Can be called from the console (base directory) with command python -m pytest
# Can NOT be called from console with same command and directory tests
# Could NOT be called with command pytest (because it does not seem to add current directory to PYTHONPATH)
#   --> this was solved by putting pytest.ini to the project

import pytest

from pkg.sub_pkg1.mod1 import add


def test_add():
    result = add(1, 2)
    assert result == 3


@pytest.mark.parametrize("arg1, arg2, result", [(1, 2, 3)])
def test_more_add(arg1, arg2, result):
    assert add(arg1, arg2) == result


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
