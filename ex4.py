lst = ["разработка", "администрирование", "protocol", "standard"]

for i in range(len(lst)):
    lst[i] = lst[i].encode('utf-8', 'replace')

    print(f"{lst[i]} ---- {type(lst[i])}")

    lst[i] = lst[i].decode('utf-8', 'replace')

    print(f"{lst[i]} ---- {type(lst[i])}\n")
