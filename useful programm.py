with open('lirics.txt', encoding="utf8") as f:
    lirics = f.read()


lirics_list = []
banned = [' ','.',',','!']
lirics_word = ''
for w in lirics:
    w = w.lower()
    if w == '\n':
        if lirics_word:
            lirics_list.append(lirics_word)
            lirics_word = ''
    elif w not in banned:
        lirics_word += w
    else:
        if lirics_word:
            lirics_list.append(lirics_word)
        lirics_word = ''
if lirics_word:
    lirics_list.append(lirics_word)
    lirics_word = ''

print(lirics_list)