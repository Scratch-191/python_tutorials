

# Path: code3.py
import sys
try:
    file_name = sys.argv[1]
except IndexError:
    print("Please provide a file name as a command-line argument.")
    sys.exit()
try:
    with open(file_name) as file:
        lines = file.readlines()
        print("Number of lines in the file:", len(lines))
except FileNotFoundError:
    print("File not found.")
    sys.exit()
except UnicodeDecodeError:
    print("Cannot read the file as it is not a text file.")
    sys.exit()
except Exception as e:
    print(e)
    sys.exit()
    

