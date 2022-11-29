def funk(text,data):
    l = list(text)
    l.sort(reverse=True)
    count = 0
    for item in l:
        if item == '0':
            count += 1
    elemet = 8 - count
    l[elemet] = str(data)
    text = ''.join(l)
    return text
text = '00600100'
print('До:')
print(text)
print('После:')
print(funk(text,5))
