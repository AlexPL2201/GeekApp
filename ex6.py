from chardet import detect


with open(file='test_file.txt', mode='rb') as f:
    txt = f.read()

encod = detect(txt)['encoding']

with open(file='test_file.txt', encoding=encod) as f:
    txt = f.read()
    print(txt)