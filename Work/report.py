# report.py
#
# Exercise 2.4
from pprint import pprint


def read_portfolio(filename: str) -> list:
    """
    Read a stock portfolio file into a list of dictionaries with the following keys:
    name, shares, and price.
    """
    portfolio = []
    with open(filename, 'rt') as f:
        skip_headers_line = next(f)

        for line in f:
            line = line.strip().replace('"', '').split(',')
            company = {
                'name': str(line[0]),
                'shares': int(line[1]),
                'price': float(line[2])
            }
            portfolio.append(company)

    return portfolio


# pprint(read_portfolio("Data/portfolio.csv"))


def calculate_total_cost(filename: str) -> int:
    """
    Calculate the total cost of the portfolio and set it to the integer
    """
    total_cost = 0
    for element in read_portfolio(filename):
        total_cost += element['shares'] * element['price']

    return total_cost


# print(f'Total cost: {calculate_total_cost("Data/portfolio.csv")}', end='\n')


def read_current_prices(filename):
    """
    Read a file with current stock prices into a list of dictionaries with the following keys:
    name, price
    """
    current_prices = []
    with open(filename, 'rt') as f:

        for line in f:
            if len(line) > 1:
                line = line.strip().replace('"', '').split(',')
                company = {
                    'name': str(line[0]),
                    'price': float(line[1])
                }
                current_prices.append(company)

    return current_prices


# pprint(read_current_prices("Data/prices.csv"))


def print_report(filename_portfolio, filename_current_prices):
    """
    Print name, shares, price, change for the stock portfolio
    """
    headers = ['Name', 'Shares', 'Price', 'Change']
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}\n'
          f'{"---------- " * len(headers)}')

    change = []
    for i in read_current_prices(filename_current_prices):
        for j in read_portfolio(filename_portfolio):
            if i['name'] == j['name']:
                diff_dict = {i['name']: i['price'] - j['price']}
                change.append(diff_dict)
                print(f'{j["name"]:>10s} {j["shares"]:>10d} {i["price"]:>10.2f} {diff_dict[i["name"]]:>10.2f}')


print(print_report('Data/portfolio.csv', 'Data/prices.csv'))
