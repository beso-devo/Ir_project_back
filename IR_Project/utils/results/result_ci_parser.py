import re


def parse_ci_result_file():
    print("Now parse_ci_result_file...")
    result = []
    ci_file_all = open("H:\PyCharm Projects\FirstOne\datasets\CISI\CISI_RESULT.txt", "r")
    content = ci_file_all.read()
    for line in content.strip().splitlines():
        # print("line = ", line)
        result.append(convert_list_string_to_int(re.split('\s+', line.strip())))
        # print("result = ", result)
    return result


def convert_list_string_to_int(list_test):
    list_test = list_test[:-2]
    for i in range(0, len(list_test)):
        list_test[i] = int(list_test[i])
    return list_test


# parse_ci_result_file()
