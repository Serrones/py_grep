from helpers import path_file

def python_grep(text, word):
    
    path = path_file(text)
    
    with open(path, 'r') as filename:
        try:
            for line_number, line in enumerate(filename):
                if word in line:
                    print(f'line {line_number} -- '
                          f'{line}'
                    )
        finally:
            print('EOF')
            filename.close
