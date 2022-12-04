import numpy as np
import os

absolute_path = os.path.dirname(__file__)

def main():
    input_file  = os.path.join(absolute_path, 'input.txt')

    acc = 0
    calories_elf = 
    with open(input_file, 'r') as f:
        for line in f.readlines():
            if('\n' != line):
                line.strip("\n")
                acc += int(line)
            elif('\n' == line):
                calories_elf.append(acc)
                acc = 0
    #part1 answer
    print(max(calories_elf)) 

    #part2 answer    
    calories_elf.sort(reverse=True)
    print(np.sum(calories_elf[0:3]))
    
if __name__ == "__main__":
    main()

