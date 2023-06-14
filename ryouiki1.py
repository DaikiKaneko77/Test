total = 0
with open('data.txt', 'r') as file:
    for line in file:
        try:
            number=int(line.strip())
            total+=number
        except ValueError:
            continue
print("合計:", total)
