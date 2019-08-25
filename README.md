# Py_Grep

On unix-like operating systems, the grep command processes
text line by line, and print any lines which match specified
pattern

Py_Grep goal is use GREP linux command behaviors to explore
Python language

### Install

create a virtual environment

`pip install requirements.txt`

### Tests

`pytest`

### Run

`from py_grep import PythonPath`

`find_word = PythonPath(file, word)`

`find_word.grep()` shows all lines with the word

`find_word.grep_line()` shows all lines enumerated with the word

`find_word.grep_count()` shows how many times the word appears

