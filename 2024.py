from pyfiglet import Figlet

magic_number = 0
for i in range(2, 10):
    magic_number += i**3

f = Figlet(font='cosmike')
print(f.renderText('2024'))
