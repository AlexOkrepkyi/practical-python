import sys


def portfolio_cost(filename):

    try:
        with open(filename, 'rt') as f:
            total_cost = 0

            headers = next(f)

            for line in f:
                line = line.strip().split(',')
                current_share = int(line[1]) * float(line[-1])  # multiply total shares by share price
                total_cost += current_share

            return f'Total cost: {total_cost}'

    except OSError as e:
        print('Oh no, looks like file with such a title does not exist!\n',
              f'ErrorMessage --> "{e}"')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

print(portfolio_cost(filename))
