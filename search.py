from os import path
import termcolor
import pathlib

excluded_extensions = [".jpg", ".png", ".jpeg", ".gif"]


def check_file_extension(filename):
    # Get the file extension
    file_extension = pathlib.Path(filename).suffix
    # Check if the file extension is part of the excluded list
    if file_extension in excluded_extensions:
        return True
    else:
        return False


def search_file(name, word):
    count = 0
    line = 0
    f = open(name, 'r')
    if f.mode == 'r':
        # Read the file content line by line
        file_content = f.readlines()
        for content in file_content:
            line += 1
            # Check if the search string is found on the line
            if word.lower() in content.lower():
                colored = content.lower()
                # Color the search string red
                colored = colored.replace(word.lower(), termcolor.colored(word.lower(), 'red'))
                # Count the occurrence of the search string on the current line
                count += content.lower().count(word.lower())
                # Print the content of the line with the colored text
                print("Line:{} {}".format(line, colored))
        if count == 0:
            print("{} was not found in {}".format(word, name))
        else:
            print("{} was found in {} {} times".format(word, name, count))
    f.close()


if __name__ == "__main__":
    file_name = input("Enter the file name or full file path: ")
    # Check if the file exists
    while not path.exists(file_name):
        file_name = input("The file does not exist, enter the file name again: ")
    excluded = check_file_extension(file_name)
    if excluded:
        print("The input file cannot be an image file, please try again with another file.")
        exit()
    search_string = input("Enter search string: ")
    search_file(file_name, search_string)
