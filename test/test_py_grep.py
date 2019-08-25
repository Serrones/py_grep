import pytest

from py_grep import PythonPath


def test_should_raise_error_if_no_file():
    with pytest.raises(FileNotFoundError):
        file = PythonPath('foobar', 'fox')
        file.grep()


def test_word_in_file(capsys):
    file = PythonPath('sample_test', 'fox')
    file.grep()
    out, err = capsys.readouterr()

    assert 'fox' in out


def test_line_number(capsys):
    file = PythonPath('sample_test', 'fox')
    file.grep_line()
    out, err = capsys.readouterr()
    
    assert 'line 3' in out
    

def test_word_count(capsys):
    file = PythonPath('sample_test', 'fox')
    file.grep_count()
    out, err = capsys.readouterr()
    
    assert '1' in out

