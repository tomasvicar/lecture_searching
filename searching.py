import os
import json

def read_data(file_name, field):
    with open(file_name) as data_file:
        data = json.load(data_file)
        print(data)
    if field in data.keys():
        return data[field]
    else:
        return None

data = read_data("sequential.json", "unordered_numbers")

# print(data)

def linear_search(numbers, searched_number):
    nalezene_pozice = []
    for pozice, number in enumerate(numbers):
        if number == searched_number:
            nalezene_pozice.append(pozice)
    vysledek = dict()
    vysledek["positions"] = nalezene_pozice
    vysledek["count"] = len(nalezene_pozice)

    return vysledek

    # for pozice in range(len(numbers)):

print(data)
print(linear_search(data, 2))
