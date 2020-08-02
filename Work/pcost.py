# pcost.py
#
# Exercise 1.27


with open('Data/portfolio.csv', 'rt') as f:
    total_cost = 0

    headers = next(f)
    print(headers)

    for line in f:
        line = line.strip().split(',')
        current_share = int(line[1]) * float(line[-1])  # multiply total shares by share price
        total_cost += current_share

    print(f'Total cost: {total_cost}')
