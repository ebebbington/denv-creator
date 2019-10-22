import os

def get_current_directory():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print(current_dir)

def add_white_spaces_at_start_of_string(text, numberOfSpaces):
    spacey_string = text.rjust(len(text)+numberOfSpaces)
    return spacey_string
spaces = add_white_spaces_at_start_of_string('hello world', 5)
print(spaces)

def get_current_file_name():
    print(__file__)

tabs = 'some text:' + '\tsome text part of the above text'
print(tabs)

print(os.getcwd() + '/../')