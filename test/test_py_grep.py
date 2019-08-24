import pytest

from py_grep import python_grep


def test_line_number_and_text(capsys):
    python_grep('sample_test', 'fox')
    
    out, err = capsys.readouterr()
    
    assert 'line 3' in out
    
def test_line(capsys):
    python_grep('sample_test', 'fox')

    out, err = capsys.readouterr()

    assert 'fox' in out
    