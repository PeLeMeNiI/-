with open('lirics.txt', encoding="utf8") as f:
    lirics = f.read()


lirics_list = []
banned = [' ','.',',','!','-']
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


check_dupes = {}
for w in lirics_list:
    w = w.lower()
    if w not in check_dupes:
        check_dupes[w] = 1
    else:
        check_dupes[w] += 1

most_freg_word = max(check_dupes.values())
for k in check_dupes.keys():
    if check_dupes[k] == most_freg_word:
        most_freg_word = k, check_dupes[k]
        break

def most_common_words(freg):
    values = freg.values()
    best = max(values)
    words = []
    for k in freg:
        if freg[k] == best:
            words.append(k)
    return words,best

def words_often(freg,times):
    result = []
    done = False
    while not done:
        temp = most_common_words(freg)
        if temp[1] >= times:
            result.append(temp)
            for w in temp[0]:
                del(freg[w])
        else:
            done = True
    return result

lirics_2000 = words_often(check_dupes,5)
   
print(lirics_2000)
