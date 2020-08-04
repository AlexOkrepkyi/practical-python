# report.py
#
# Exercise 2.4


def portfolio_cost(filename1, filename2):

    with open(filename1, 'rt') as f:
        portfolio = []
        total_cost = 0
        skip_headers_line = next(f)

        for line in f:
            line = line.strip().replace('"', '').split(',')
            company = {'name': str(line[0]), 'shares': int(line[1]), 'price': float(line[2])}
            portfolio.append(company)

        for element in portfolio:
            total_cost += element['shares'] * element['price']

    print(portfolio)

    with open(filename2, 'rt') as f:
        current_prices = []

        for line in f:
            if len(line) > 1:
                line = line.strip().replace('"', "").split(',')
                company = {'name': str(line[0]), 'price': float(line[1])}
                current_prices.append(company)

    headers = ['Name', 'Shares', 'Price', 'Change']

    print(f'{headers[0]}\t{headers[1]}\t{headers[2]}\t{headers[3]}\n'
          f'-------\t-------\t-------\t-------')

    change = []
    for i in current_prices:
        for j in portfolio:
            if i['name'] == j['name']:
                diff_dict = {i['name']: i['price'] - j['price']}
                change.append(diff_dict)
                print(f'{j["name"]}\t{j["shares"]}\t{i["price"]}\t{diff_dict[i["name"]]:0.2f}')


print(portfolio_cost('Data/portfolio.csv', 'Data/prices.csv'))
