import pyfiglet
from datetime import datetime

happy = ''.join([chr(x) if x != 112 else chr(x)*2 for x in [72, 97, 112, 121]])
new = datetime.now()
print(pyfiglet.figlet_format(f'{happy} {new.year}!'))

# https://github.com/pwaller/pyfiglet
# pyfiglet --list_fonts