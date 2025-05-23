my_list = [1, 2, 3, 4, 5, 2, 6, 7, 3]

duplicates = set()
seen = set()

for item in my_list:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

if duplicates:
    print("Есть повторяющиеся элементы:")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("Повторяющихся элементов нет.")
