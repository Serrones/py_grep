import pytest
from pathlib import Path

from helpers import path_file


@pytest.fixture
def get_path_file():
    path_test = path_file('file')

    return path_test

def test_path_file(get_path_file):
    path = Path
    path_to_dir = path.cwd()
    path_test = get_path_file    

    assert path_to_dir.as_posix() == path_test.as_posix()[0:-5]

def test_file_should_be_in_path(get_path_file):
    assert 'file' == get_path_file.name
