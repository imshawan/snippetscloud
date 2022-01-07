'''
    Author:      Shawan Mandal
    Description: Takes the filename or the file path (incase in different directory), encodes into base64
                 string and writes it to a file.
'''

import base64

def beautify(base64_data, language):
    '''
    This function generates a more prettier way of storing the string to a file by giving proper line breaks.
    '''
    types = {
        'python': '"\\', # Arrangement according to python syntax
        'javascript': '"+', # Arrangement according to JavaScript syntax
        'other': '"+'
    }
    LINE_BREAK = 130 #After 130 chars, it will give a linebreak
    processed_data = ""
    pos = 0
    new_data = ""
    last = 0
    length = len(base64_data)
    # Arranging the base64 data with proper line breaks
    while pos <= length:
        last = pos + LINE_BREAK
        if last > length:
            last = length
        for x in range(pos, last, 1):
            new_data = new_data + base64_data[x]
        processed_data = processed_data + '"' + new_data + types[language] + "\n"
        # Replace javascript with your preffered output language style
        new_data = ""
        pos = pos + LINE_BREAK
    return processed_data[:len(processed_data)-2]


filename = input("Enter Filename: ")
outputFile = f'{filename}.txt'

with open(filename, 'rb') as _file:
    file_data = _file.read()
    base64_encoded_data = base64.b64encode(file_data)
    base64_data = base64_encoded_data.decode('utf-8')

processed = beautify(base64_data, 'python') # Adds proper line breaks according to a particular language

with open(outputFile, 'w') as _file:
    _file.write(processed)

input("Done! Press any key to continue...")
