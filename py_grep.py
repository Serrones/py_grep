import os

def python_grep(text, word):
    path_file = os.getcwd()
    file = path_file + '/' + text
    with open(file, 'r') as filename:
        try:
            for line in filename:
                if word in line:
                    print(line)
        finally:
            print('EOF')
            filename.close
