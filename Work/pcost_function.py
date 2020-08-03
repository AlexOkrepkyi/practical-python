import sys


def portfolio_cost(filename):

    with open(filename, 'rt') as f:
        portfolio = []
        total_cost = 0
        headers = next(f)

        for line in f:
            line = line.strip().replace('"', '').split(',')
            company = (str(line[0]), int(line[1]), float(line[2]))
            portfolio.append(company)

        for title, shares, price in portfolio:
            total_cost += shares * price

        return f'Portfolio --> {portfolio}\n' \
               f'Total cost --> {total_cost}'


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print(portfolio_cost(filename))
