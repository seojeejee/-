file_path = "Mars_Base_Inventory_List.csv"

csv_list = []
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    headers = lines[0].strip().split(',')

    for line in lines[1:]:
        values = line.strip().split(',')
        item = dict(zip(headers, values))
        try:
            item['Flammability'] = float(item['Flammability'])
        except (ValueError, TypeError):
            item['Flammability'] = 0
        csv_list.append(item)

sort_list = sorted(csv_list, key=lambda x: x['Flammability'], reverse=True)

dangerous = [item for item in sort_list if item['Flammability'] >= 0.7]

dangerous_file = "Mars_Base_Inventory_danger.csv"
with open(dangerous_file, 'w', encoding='utf-8') as f:
    f.write(','.join(headers) + '\n')  # 헤더 쓰기
    for item in dangerous:
        row = [str(item.get(header, '')) for header in headers]
        f.write(','.join(row) + '\n')

print("인화성이 높은 5개 품목")
for item in sort_list[:5]:
    print(item)

print("\n인화성 0.7 이상 품목")
for item in dangerous:
    print(item)
