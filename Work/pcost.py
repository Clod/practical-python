# pcost.py
#
# Exercise 1.27

#import os
import sys

# print ("Current directory: ", os.getcwd())
def portfolio_cost(filename):
    total = 0
    # with open('Work/Data/portfolio.csv', 'rt') as f:
    with open(filename, 'rt') as f:
        next(f)
        for line in f:
            row = line.split(',')
            try:
                total += float(row[1]) * float(row[2])
            except ValueError:
                print('Could not parse: ', line)
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work/Data/portfolio.csv'

total = portfolio_cost(filename)
print("Total cost ", round(total, 2))
