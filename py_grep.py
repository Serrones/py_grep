from helpers import path_file

def python_grep(text, word):
    
    path = path_file(text)
    
    with open(path, 'r') as filename:
        try:
            for line in filename:
                if word in line:
                    print(line)
        finally:
            print('EOF')
            filename.close
