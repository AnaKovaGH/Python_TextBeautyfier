import re


#функція для корегування кількості символів в рядку
def create_transfers(input_string):
    mas = input_string.split(" ")
    result = ""
    current_lenth = 0
    for word in mas:
        if current_lenth + len(word) > given_lenth:
            result += "\n"
            current_lenth = 0
            mas.insert(0,word)
        else:
            result += word + " "
            current_lenth += len(word) + 1
    return result


#функція для заміни лапок
def replace_brackets(word):
    first_brac =  re.match('"', word)
    if first_brac != None:
        smb = first_brac.group()
        word = word[:first_brac.start()+1].replace("\"","``") + word[first_brac.start()+1:]

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

#функція для додавання слешу
def add_slash(word):
    smb = {"$", "%", "[", "]", "{", "}", "(", ")"}
    for i in smb:
        if word.find(i) != -1:
          tmp =  word.find(i)
          word = word[:tmp] + word[tmp:].replace(i, "\\"+ i)

    return word






print("Task 2\n")
given_lenth = 80
input_file = open("text_file_task2.txt", "r")
output_file = open("new_file_task2.txt", "w")

ready_words = []
for line in input_file:
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
        prom = prom[size+1:]
        string += "\n\n\n"
tmp = create_transfers(string)
output_file.write(tmp)

input_file.close()
output_file.close()
