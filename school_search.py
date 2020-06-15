import itertools
from csv import DictReader
import os
import time
import re
root_path = os.path.abspath(os.path.dirname(__file__))
# file_location = root_path + '/school_data.csv'
ignore_words = ("ELEMENTARY","HIGH","MIDDLE","SCHOOL","KINDERGARTEN")
school_column_name = "SCHNAM05"
city_column = "LCITY05"
state_column = "LSTATE05"
school_text = input("enter the text - ")
school_text = "riverside school 44"
start_time = time.clock()


def search_schools(school_text):
    school_dict = {}
    return_list = []
    count = 0
    file_location = root_path + '/school_data.csv'
    school_file = open(file_location, 'r', encoding='ISO-8859-1')
    school_data = DictReader(school_file)
    sorted_school_data = sorted(school_data, key=lambda d: d[school_column_name])

    t = school_text.upper().split(" ")
    search_words = [e for e in t if e not in ignore_words]
    search_string  = ' '.join([i for i in search_words])

    for row in sorted_school_data:
        if search_string in row[school_column_name]:
            school_dict[row[school_column_name]] = [row[state_column], row[city_column]]
        if any(x in row[school_column_name] for x in search_words) and any(x in row[city_column] for x in search_words):
            school_dict[row[school_column_name]] = [row[state_column], row[city_column]]
        if all(x in row[school_column_name] for x in search_words):
            school_dict[row[school_column_name]] = [row[state_column], row[city_column]]
    sorted_dict =  sorted(school_dict.items(), key=lambda d: d[0] )

    for t in search_words:
        for k,v in sorted_dict:
            if search_string in k and k not in return_list:
                return_list.append([k, v])
            if t in k and k not in return_list:
                return_list.append([k, v])

    time_taken = (time.clock() - start_time)
    print("Results for {} (search took: {}s".format(school_text, time_taken))

    for row in sorted_school_data:
        if school_text.upper() == row[school_column_name]:
            count += 1
            print("{}. {} \n {}, {}".format(count, row[school_column_name], row[city_column], row[state_column]))

    for schools in return_list:
        count += 1
        print("{}. {} \n {}, {}".format(count, schools[0], schools[1][1], schools[1][0]))
        if count == 3:
            break


search_schools(school_text)
