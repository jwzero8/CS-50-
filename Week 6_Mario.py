# TODO
# I have made reference from youtube after the part of break
import cs50

while True:
    height = cs50.get_int('Height: ')
    if height >= 1 and height <= 8:
        break

for row in range(1, height + 1):
    print(' ' * (height - row) + '#' * row)
