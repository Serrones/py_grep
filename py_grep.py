from helpers import path_file

def python_grep(text, word):
    
    path = path_file(text)
    
    try:
        with open(path, 'r') as filename:
            for line_number, line in enumerate(filename):
                if word in line:
                    print(f'line {line_number} -- '
                          f'{line}'
                    )
            filename.close
    except FileNotFoundError as error:
        print('There is no file with this name')
    finally:
        print('Finished')

