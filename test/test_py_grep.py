import pytest

from py_grep import python_grep


def test_line_number(capsys):
    python_grep('sample_test', 'fox')
    
    out, err = capsys.readouterr()
    
    assert 'line 3' in out
    
def test_word_in_file(capsys):
    python_grep('sample_test', 'fox')

    out, err = capsys.readouterr()

    assert 'fox' in out
    
def test_should_raise_error_if_no_file(capsys):
    message = 'There is no file with this name'
    python_grep('foobar', 'fox')

    out, err = capsys.readouterr()

    assert message in out