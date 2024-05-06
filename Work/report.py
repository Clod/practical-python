# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_portfolio_dict(filename):

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {}
            holding[headers[0]] = row[0]
            holding[headers[1]] = int(row[1])
            holding[headers[2]] = float(row[2])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):

    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if (len(row) > 0):
                prices[row[0]] = float(row[1]) 
    return prices

def make_report(stocks, prices):
    report = []
    prices = read_prices('Data/prices.csv')
    stocks = read_portfolio_dict('Data/portfolio.csv')
    for line in stocks:
        #print(line, prices[line['name']], line['price'] - prices[line['name']])
        #tupla = (line['name'], line['shares'], prices[line['name']],line['price'] - prices[line['name']])
        report.append((line['name'], line['shares'], prices[line['name']],line['price'] - prices[line['name']]))
    return report

#print(read_prices('Data/prices.csv'))
stocks = []
prices = {}

report = make_report(stocks, prices)

'''
for r in report:
    print('%10s %10d %10.2f %10.2f' % r)
'''

headers = ('Name', 'Shares', 'Price', 'Change')

print(f'{headers[0]:>10s}{headers[1]:>11s}{headers[2]:>11s}{headers[3]:>11s}')
#print(f'{"-" * len(headers[0]):>10s}{"-" * len(headers[1]):>11s}{"-" * len(headers[2]):>11s}{"-" * len(headers[3]):>11s}')
print('---------- ---------- ---------- -----------')

for name, shares, price, change in report:
    #print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
    print(f'{name:>10s} {shares:>10d} {"$"+str(price):>10s} {change:>10.2f}')

