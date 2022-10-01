stringList = ["class", "function", "method"]
byteList = []

for s in stringList:
    s = eval(f"b'{s}'")
    byteList.append(s)

for b in byteList:
    print(f"{b} ---- {type(b)} ---- {len(b)}")
