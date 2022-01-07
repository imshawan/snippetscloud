'''
    Author:      Shawan Mandal
    Function:    decode_base64_data(filepath)
    Description: Takes the filename or the file path (incase in different directory), decodes the base64
                 encoded string back to the original file
'''
import base64

def decode_base64_data(filepath):
    with open(filename, 'r') as _file:
        base64_data = _file.read()
    base64_img_bytes = base64_data.encode('utf-8')
    with open('decoded_file', 'wb') as file_to_save:
        # After decoding the file, add the specific extension to that file.
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)

filename = input("Enter Filename: ")
decode_base64_data(filename)
