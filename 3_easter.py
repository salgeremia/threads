text = 'HappyEasterEgg!'

i, raw = 0, 0
while True:
    raw += 1
    for _ in range(raw):
        if i < len(text):
            print(text[i], end=' ')
            i += 1
        else:
            break
    else:
        print()
        continue
    break