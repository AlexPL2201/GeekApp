stringList = ["attribute", "клaсс", "функция", "type"]
byteList = []

for s in stringList:
    try:
        s = eval(f"b'{s}'")
        byteList.append(s)
    except SyntaxError:
        print(f"Ошибка. Строку '{s}' нельзя преобразовать в байтовый тип!!!")


for b in byteList:
    print(f"{b} ---- {type(b)} ---- {len(b)}")
