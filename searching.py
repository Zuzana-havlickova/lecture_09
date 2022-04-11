import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field not in set(data.keys()):
        return None
    return data[field]

def linear_search(sequence, number):
   sumation = 0
   num_index = []
   for i, nmbr in enumerate(sequence):
       if nmbr == number:
           sumation += 1
           num_index.append(i)
   slovnik = {"indexy": num_index, "cetnost": sumation}
   return slovnik

def pattern_search(sekvence, vzor):
   positions = set()
   index = 0
   while index < len(sekvence) - len(vzor):
       idx = 0
       for letter in sekvence[index:index + len(vzor)]:
           if letter != vzor[idx]:
               break
           else:
               idx = idx + 1
       if idx == len(vzor):
           positions.add(index)
       index = index + 1
   return positions


def binary_search(seznam, cislo):
    left = 0
    right = len(seznam) - 1
    while left < right:
        middle = (left + right) // 2
        if seznam[middle] == cislo:
            return middle
        elif seznam[middle] < cislo:
            left = middle + 1
        elif seznam[middle] > cislo:
            right = middle -1
    return None


def main():
    #sequential_data = read_data("sequential.json", "unordered_number")
    #sequential_data = read_data("sequential.json", "dna_sequence")
    sequential_data = read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    #print(linear_search(sequential_data, number))
    #print(pattern_search(sequential_data, vzor))
    print(binary_search(sequential_data, cislo))


if __name__ == '__main__':
    #number = 9
    #vzor = "ATA"
    cislo = 14
    main()







