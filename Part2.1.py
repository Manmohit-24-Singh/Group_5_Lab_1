'''
i)  The function of this code is to find the roots of a quadratic equation. It checks if
    the value under the square root for the quadratic formula is above zero and if so
    initiates the code accordingly.

ii) The error in the code was during the print statements where the opening quotation (')
    was closed with an apostrophe (’) instead of a closing quotation and therefore the code
    could not run due to the syntax error.
'''

import sys
import math
def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = b**2 - 4*a*c
    print(f'D is equal to {d}')
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')

do_stuff()