# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''

import sys
from random import seed, randint
from math import gcd

try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)
# L = [0]
# L = [0, 0]
# L = [1]
# L = [0,1]
# L = [1, 2, 0, 5, 3]
# L = [6, 12, 6]
# L = [12, 13, 1]
# L = [4, 18, 27, 25]
# L = [3, 2, 5]
# L = [49, 97, 53]
# L = [27, 12, 24, 28, 13]
# L = [24, 26, 2, 16]

fractions = []
spot_on, closest_1, closest_2 = [None] * 3
#####
L2 = []
from fractions import Fraction
from heapq import nsmallest

for numerator in L:
    for denominator in L:
        if numerator > denominator or denominator == 0:
            continue
        L2.append(Fraction(numerator, denominator))

# Sort the list and remove duplicates
L2 = sorted(set(L2))

# Check for corner case where only one element in the list
if len(L2) > 1:
    closest_1, closest_2 = nsmallest(2, L2, key=lambda x: abs(x - 0.5))
    if closest_1 + closest_2 != 1:
        closest_2 = None
elif len(L2) == 1:
    closest_1 = L2[0]
else:
    L2 = [0]
    closest_1 = L2[0]

for i in L2:
    if i == Fraction(1, 2):
        spot_on = True
    fractions.append(str(i))

#####
print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')
