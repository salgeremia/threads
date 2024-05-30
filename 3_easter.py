text = 'HappyEasterEgg!'

i, row = 0, 0
while True:
    row += 1
    for _ in range(row):
        if i < len(text):
            print(text[i], end=' ')
            i += 1
        else:
            break
    else:
        print()
        continue
    break