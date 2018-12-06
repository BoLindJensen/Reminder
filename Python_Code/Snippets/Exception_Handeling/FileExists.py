'''
Pythons EAFP approach to Exception handeling
(it's Easier to Ask Forgiveness than Permission')
'''

path = '/path/to/file.dat'

try:
    process_file(path)
except OSError as e:   #  Exception handler catching everything that possible could go wrong, file not there, path was for directory... etc
    print(f'Could not process file because{e}')


def process_file(file_input_path):
    # ...
    # perform Some logic for processing files
    # ...
    pass
