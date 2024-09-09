# This program is a simple file type detector that uses pattern matching to determine the file type based on the file extension. Itreads the file name from the user and then uses pattern matching to determine the file type based on the file extension. If the file extension is not recognized, the program prints "application/octet-stream" to the console. It uses the match statement to match the file extension to the corresponding file type.
def main():
    filename = input('File name: ').strip().lower()

    if '.' not in filename:
        print('application/octet-stream')
        return

    extension = filename.split('.')[-1]

    match(extension):
        case 'gif':
            print('image/gif')
        case 'jpg':
            print('image/jpeg')
        case 'jpeg':
            print('image/jpeg')
        case 'png':
            print('image/png')
        case 'pdf':
            print('application/pdf')
        case 'txt':
            print('text/plain')
        case 'zip':
            print('application/zip')
        case _:
            print('application/octet-stream')
main()
