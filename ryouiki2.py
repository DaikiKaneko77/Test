import json

count = 0
max_price = float('-inf')
min_price = float('inf')

with open('catalog.json', 'r') as file:
    data = json.load(file)
    for item in data:
        if item['name'] == 'jacket':
            count += 1
            price = item['price']
            if price > max_price:
                max_price = price
            if price < min_price:
                min_price = price

print("Jacketの個数:", count)
print("最高価格:", max_price)
print("最低価格:", min_price)
