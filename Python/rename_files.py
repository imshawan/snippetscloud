'''
    Author:      Shawan Mandal
    Description: Renames files in a particular folder in bulk. (Useful in renaming file extensions and stuffs like that)
'''

import os

def rename_files(new_name, src = os.getcwd()):
    '''Takes new file name and the output path as parameter'''
    files_list = os.listdir()
    name = ""
    for file_name in files_list:
        if file_name[:2]=='py': # Do not modify the script (python *.py) file
            pass
        else:
            if new_name == "":
                name = file_name
            else:
                name =  new_name
            src = os.path.join(src, file_name)
            os.rename(src, name)
            src = ""

def change_file_extension(new_ext, src = os.getcwd()):
    '''Takes new file extension and the output path as parameter'''
    files_list = os.listdir()
    name = ""
    for file_name in files_list:
        if file_name[:2]=='py': # Do not modify the script (python *.py) file
            pass
        else:
            if new_name == "":
                name = file_name
            else:
                name = file_name + new_ext
            src = os.path.join(src, file_name)
            os.rename(src, name)
            src = ""