import sys


def portfolio_cost(filename):

    with open(filename, 'rt') as f:
        portfolio = []
        total_cost = 0
        headers = next(f)

        for line in f:
            line = line.strip().replace('"', '').split(',')
            company = {'name': str(line[0]), 'shares': int(line[1]), 'price': float(line[2])}
            portfolio.append(company)

        for element in portfolio:
            total_cost += element['shares'] * element['price']

        return f'Portfolio --> {portfolio}\n' \
               f'Total cost --> {total_cost}'


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print(portfolio_cost(filename))
