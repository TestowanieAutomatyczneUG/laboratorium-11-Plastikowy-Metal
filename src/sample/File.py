import os

class File:
    def __init__(self, file):
        self.file_name = file

    def read_file(self):
        with open(self.file_name, 'r') as file:
            return file.read()

    def write_file(self, data):
        with open(self.file_name, 'w') as file:
            file.write(data)

    def delete_file(self):
        if not os.path.isfile(self.file_name):
            raise (Exception, 'File NOT found')
        else:
            os.remove(self.file_name)
