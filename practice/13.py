#!/bin/python3

def solve(s):
    words = s.split(' ')
    cap = [word.capitalize() for word in words]
    cap = ' '.join(cap)
    return cap

if __name__ == '__main__':
    # Specify the output file path directly
    output_path = 'output.txt'

    # Open the file in write mode
    with open(output_path, 'w') as fptr:
        # Read input from the user
        s = input("Enter a string: ")
        
        # Process the string
        result = solve(s)
        
        # Write the result to the file
        fptr.write(result + '\n')

    print(f"Result has been written to {output_path}")
