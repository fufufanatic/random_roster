'''
Created by fufufanatic
random_roster.py randomizes/reorders the line items of a text file
'''

import random
import sys

# Main method that shuffles the line items of a file. Parameter is a file path.
def randomize_me(file):    

    lines = []
    
    # Opens the specified file, reads each line item, strips away whitespace (beginning and trailing), and places line item in array.
    print('\n===== Randomizer [Reading] =====\n')
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            print(f'- {line}')
            lines.append(line)

    # Shuffles the line items within the array (parameter)
    random.shuffle(lines)

    # Re-opens same file, deletes its entire content, and replaces with line items from the randomized array.
    print('\n===== Randomizer [Writing] =====\n')
    with open(file, 'w') as f:
        for line in lines:
            print(f'+ {line}')
            f.write(f'{line}\n')

def main():

    # Runs the main program; assumes any error is due to poor syntax and provides an example for running script in terminal.
    try:
        randomize_me(sys.argv[1])
    except Exception:
        print('\nOops! something went wrong ... Run script like so:')
        print('python random_roster.py <roster file path>\n')

if __name__ == '__main__':
    main()