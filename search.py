from os import path
import termcolor


def search_file(name, word):
    count = 0
    f = open(name, 'r')
    if f.mode == 'r':
        file_content = f.readlines()
        for content in file_content:
            if word.lower() in content.lower():
                colored = content.lower()
                colored = colored.replace(word.lower(), termcolor.colored(word.lower(), 'red'))
                count += content.lower().count(word.lower())
                print(colored)
        if count == 0:
            print("{} was not found in {}".format(word, name))
        else:
            print("{} was found in {} {} times".format(word, name, count))
    f.close()


if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    while not path.exists(file_name):
        file_name = input("The file does not exist, enter the file name again: ")
    search_string = input("Enter search string: ")
    search_file(file_name, search_string)
