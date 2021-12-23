'''
Created by fufufanatic
random_roster.py randomizes/reorders the line items of a text file
'''

import random
import sys

def randomize_me(file):    

    lines = []
    
    print('\n===== Randomizer [Reading] =====\n')
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            print(f'- {line}')
            lines.append(line)

    random.shuffle(lines)

    print('\n===== Randomizer [Writing] =====\n')
    with open(file, 'w') as f:
        for line in lines:
            print(f'+ {line}')
            f.write(f'{line}\n')

def main():
    try:
        randomize_me(sys.argv[1])
    except:
        print('\nOops! something went wrong ... Run script like so:')
        print('python random_roster.py <roster file path>\n')

if __name__ == '__main__':
    main()