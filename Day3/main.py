import numpy as np
import os
from itertools import islice

def calculate_priorities(repeated_types):
    sum = 0
    for c in repeated_types:
        if(c.islower()) :
            x = ord(c[2]) - 96
            sum += x 
        if(c.isupper()) :
            x = ord(c[2]) - 38
            sum += x
    return sum

def get_item_common_both(input_file):

    repeated_types = list()

    with open(input_file, 'r') as f:
        for line in f.readlines():
            string1 = line[:len(line)//2]
            string2 = line[len(line)//2:]
            print(string1,string2)
            print(set(string1).intersection(string2))
            repeated_types.append(str(set(string1).intersection(string2)))
    return repeated_types
    

def get_item_in_three_compartments(input_file):

    repeated_types = list()

    with open(input_file, 'r') as f:
        while True:
            next_n_lines = list(islice(f, 3))
            if not next_n_lines:
                break
            group_of_lines=[line.strip() for line in next_n_lines]
            repeated_types.append(str(set(group_of_lines[0]).intersection(group_of_lines[1],group_of_lines[2])))
    return repeated_types



def main():
    input_file  = os.path.join(os.path.dirname(__file__), 'input.txt')

    #Part1
    repeated_types = get_item_common_both(input_file)
    print(repeated_types)
    sum = calculate_priorities(repeated_types)
    print(sum)

    #Part2
    repeated_types = get_item_in_three_compartments(input_file)
    print(repeated_types)
    sum = calculate_priorities(repeated_types)
    print(sum)



if __name__ == "__main__":
    main()