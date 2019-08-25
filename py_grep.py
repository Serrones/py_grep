from helpers import path_file

class PythonPath:
    def __init__(self, text, word):
        self.path = path_file(text)
        self.word = word
        
    
    def _grep(self):
        try:
            self.filename = open(self.path, 'r')
        except FileNotFoundError as error:
            raise error


    def grep(self):
        file = self._grep()
        for line in self.filename:
            if self.word in line:
                print(f'{line}')
        self.filename.close()


    def grep_line(self):
        file = self._grep()
        for line_number, line in enumerate(self.filename):
            if self.word in line:
                print(f'line {line_number} -- '
                        f'{line}'
                )
        self.filename.close()
    

    def grep_count(self):
        file = self._grep()
        count_word = 0
        for line in self.filename:
            if self.word in line:
                count_word += 1
        print(f'Word "{self.word}" appears '
              f'{count_word} times'
        )
        self.filename.close()
