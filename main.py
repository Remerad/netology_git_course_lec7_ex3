
text_files_dict = {"1.txt": 0, "2.txt": 0, "3.txt": 0}  #Файлы и количество строк в них
text_files_order = []


def text_files_lines_counter():
    for f in text_files_dict.keys():
        print(f)
        with open(f, 'r', encoding='utf-8') as ff:
            my_lines = list(ff)
        text_files_dict.update({f: len(my_lines)})
    print(text_files_dict)


def get_text_files_order():
    text_files_order.extend(sorted(text_files_dict, key=lambda k: text_files_dict[k]))


def write_result_file():
    with open("result_file", 'w', encoding='utf-8') as rf:
        pass
    for i in text_files_order:
        with open("result_file", 'a',  encoding='utf-8') as rf:
            rf.write(i+"\n")
            rf.write(str(text_files_dict[i])+"\n")
            with open(i, 'r', encoding='utf-8') as ff:
                while True:
                    line = ff.readline()
                    if not line:
                        rf.write("\n")
                        break
                    rf.write(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    text_files_lines_counter()
    get_text_files_order()
    print(text_files_order)
    write_result_file()
