from os import path
import getopt, sys
import termcolor, colorama
import pathlib
import re
import time

# Invalid file extensions
invalid_extensions = [".jpg", ".png", ".jpeg", ".gif"]


def usage():
    """
    Prints usage of file
    """
    print("Usage search.py -i <input-file> -s <search-string> -c <case sensitive 1> or <case insensitive 2> -h")


def usage_help():
    usage()
    print("-i : This option defines the input file name to be searched through")
    print("-s : This option defines the word or phrase which we need to search")
    print(" (Ex: \"sample word\")")
    print("-c : This option defines if the search is case sensitive or not.")
    print("use 1 for case sensitive search and 2 for case insensitive search")
    print("-h : Help.")


def check_file_extension(filename):
    """
       checks for valid file extensions.

       Parameters:
           filename (str):The name of the file.

       Returns:
           True: If file extension is not valid
           False: If file extension is valid
    """
    file_extension = pathlib.Path(filename).suffix
    if file_extension in invalid_extensions:
        return True
    else:
        return False


def convert_to_lowercase(string):
    """
    Convert string to lowercase
    :param string: String to be converted
    :return string: Converted String
    """
    return string.lower()


def colour_search_string(line, search_string):
    """
    Returns colored String.

    Parameters:
        line (str):The string which is to be colored.
        search_string (str): The part of the string to be colored

    Returns:
        colored_string (str):The string that was colored.
    """
    colorama.init()
    colored_string = line.replace(search_string, termcolor.colored(search_string, 'red'))
    return colored_string


def count_word(line, string):
    """
    Counts number of occurrence of string on the line.

    Parameters:
        line (str):The line containing the string pattern to be counted.
        string (str): The string pattern which is to be counted

    Returns:
        count (int):Total number counted.
    """
    count = line.count(string)

    return count


def regex_search(name, word, option):
    """
    Searches for a string within a file using Regex

    Parameters:
        name: The file to be searched.
        word: The string that is being searched
        option: Case sensitivity option
    """
    line_number = 0
    its_found = 0
    compile_string = re.compile(word)
    file = open(name, 'r', encoding='utf-8')
    for line in file:
        line_number += 1
        if option == 2:
            line = convert_to_lowercase(line)
        if word in compile_string.findall(line):
            colored = colour_search_string(line, word)
            word_count = count_word(line, word)
            print("Line{} found {}: {}".format(line_number, word_count, colored))
            its_found += 1
    if its_found == 0:
        print("{} was not found in {}".format(word, name))
    file.close()


def search_file(name, word, option):
    """
    Searches for a string within a file

    Parameters:
        name: The file to be searched.
        word: The string that is being searched
        option: Case sensitivity option
    """
    line = 0
    its_found = 0
    file = open(name, 'r', encoding='utf-8')
    if file.mode == 'r':
        for content in file:
            line += 1
            if option == 2:
                content = convert_to_lowercase(content)
            if word in content:
                content = colour_search_string(content, word)
                word_count = count_word(content, word)
                print("Line{} found {}: {}".format(line, word_count, content))
                its_found += 1
        if its_found == 0:
            print("{} was not found in {}".format(word, name))
    file.close()


def main(argv):
    if len(argv) < 1:
        usage()
        exit()
    elif len(argv) == 1 and argv[0] != "-h":
        usage()
        exit()
    elif 1 < len(argv) < 6:
        usage()
        exit()

    try:
        opts, args = getopt.getopt(argv, "hi:s:c:", ["ifile=", "sstring=", "coption"])
    except getopt.GetoptError:
        usage()
        exit(2)
    for opt, arg in opts:
        if opt in "-h":
            usage_help()
            exit(2)
        elif opt in ("-i", "--ifile"):
            file_name = arg
        elif opt in ("-s", "--sstring"):
            search_string = arg
        elif opt in ("-c", "--coption"):
            case_option = arg
        else:
            usage()
            exit(2)

    while not path.exists(file_name):
        exit("File not found")

    invalid_extension = check_file_extension(file_name)
    if invalid_extension:
        exit("The input file cannot be an image file, please try again with another file.")

    search_string = search_string.rstrip()
    case_option = int(case_option)
    if case_option not in [1, 2]:
        exit("Invalid option selected, try again!!")
    if case_option == 2:
        search_string = convert_to_lowercase(search_string)

    search_method = input("Enter 1 for regex search or 2 for regular search: ")
    search_method = int(search_method)
    if search_method == 1:
        start_time = time.time()
        regex_search(file_name, search_string, case_option)
        end_time = time.time()
        print("Regex search took %s seconds" % (end_time - start_time))
    elif search_method == 2:
        start_time = time.time()
        search_file(file_name, search_string, case_option)
        end_time = time.time()
        print("Regular search took %s seconds" % (end_time - start_time))
    else:
        print("You entered the wrong option")
        exit()


if __name__ == "__main__":
    argument_list = sys.argv[1:]
    main(argument_list)
