from __future__ import print_function
import re
import argparse
import sys
__author__ = "AnnieKey, MasterBob (BopOnTheTop)"
__license__ = "MIT"

"""
A python tool to make copy-pasted text look nicely in LaTeX.
Basically, it needs to read a file in order to produce nice output. 
Reading from pipes was not planned from the early development stage 
and does not fin in current paradigm. 
Supports though,  bare-console  output, as well as writing to file.
        K.I.S.S. methodology as-is.
                                    - MasterBob
"""


given_lenth = 80


def create_transfers(input_string):
    """
    функція для корегування кількості символів в рядку
    :param input_string:
    :return:
    """
    mas = input_string.split(" ")
    result = ""
    current_lenth = 0
    for word in mas:
        if current_lenth + len(word) > given_lenth:
            result += "\n"
            result += word + " "
            current_lenth = len(word)
        else:
            result += word + " "
            current_lenth += len(word) + 1
    return result


# функція для заміни лапок
def replace_brackets(word):
    first_brac = re.match('"', word)
    if first_brac is not None:
        word = word[:first_brac.start() + 1].replace("\"", "``") + word[first_brac.start() + 1:]

    tmp = word.rfind("\"")
    if tmp != -1:
        tmp_st = word[tmp:]
        if tmp_st[-1] == "\"":
            word = word[:tmp] + word[tmp:].replace("\"", "''")
        elif tmp_st[-1] == "." or tmp_st[-1] == ",":
            word = word[:tmp] + word[tmp:tmp + 1].replace("\"", "''") + tmp_st[-1]

    prom1 = word.find("«")
    if prom1 != -1:
        word = word[:prom1] + word[prom1:].replace("«", "``")
    prom2 = word.find("»")
    if prom2 != -1:
        word = word[:prom2] + word[prom2:].replace("»", "''")

    return word


# функція для додавання слешу
def add_slash(word):
    smb = {"$", "%", "[", "]", "{", "}", "(", ")"}
    for i in smb:
        if word.find(i) != -1:
            tmp = word.find(i)
            word = word[:tmp] + word[tmp:].replace(i, "\\" + i)

    return word


def beautify(input_lines):

    output = ""
    ready_words = []
    for line in input_lines:
        if line[-1] != "\n":
            line += "\n"
        words = line.split(" ")
        for i in words:
            word = replace_brackets(i)
            ready_words.append(add_slash(word))

    prom = " ".join(ready_words)
    string = ""
    size = 0
    for i in prom:
        if i != "\n":
            string = string + i
            size = len(string)
        else:
            tmp = create_transfers(string)
            output += tmp
            prom = prom[size + 1:]
            string = "\n\n\n"
    return output

##
# Argument parsing section
##

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="A file which to translate")
parser.add_argument("-d", "--destinaton", help="Output file, where to write beautified text."
                                              "If not specified, text is printed to STDOUT")
args = parser.parse_args()
if args.input is None:
    print("[!] Error! Input file not specified.", file=sys.stderr)
    exit(1)
else:
    try:
        input_file = open(args.input, "r")
    except OSError as e:
        print("[!] Error! {msg}".format(msg=e.strerror), file=sys.stderr)
        exit(code=e.errno)

    input_lines_list = []
    for line in input_file:
        input_lines_list += [line]
    input_file.close()
    if args.destinaton is None:
        print(beautify(input_lines=input_lines_list))

    else:
        try:
            output_file = open(args.destinaton,"w")
        except OSError as e:
            print("[!] Error! {msg}".format(msg=e.strerror), file=sys.stderr)
            exit(code=e.errno)
        output_file.write(beautify(input_lines=input_lines_list))
        output_file.close()
