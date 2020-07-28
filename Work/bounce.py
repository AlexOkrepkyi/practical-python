# bounce.py
#
# Exercise 1.5


start_height = 100
amortisation = 1 * 3 / 5
bounce       = 1

for _ in range(10):
    current_height = start_height * amortisation
    print(bounce, round(current_height, 4))
    bounce += 1
    start_height = current_height
