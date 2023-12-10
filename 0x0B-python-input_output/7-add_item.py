#!/usr/bin/python3
""" Module to save json file """


import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = []
args = sys.argv[1:]

filename = "add_item.json"

if not path.exists(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

my_list.extend(args)

save_to_json_file(my_list, filename)
