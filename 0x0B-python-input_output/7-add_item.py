#!/usr/bin/python3
import sys
from os import path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args = sys.argv[1:]

filename = "add_item.json"

if not path.exists(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

my_list.extend(args)

save_to_json_file(my_list, filename)
