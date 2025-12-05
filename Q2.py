arr = [12, 45, 7, 23, 89, 34]

min_ele = arr[0]
max_ele = arr[0]

for i in arr:
    if i < min_ele:
        min_ele = i
    if i > max_ele:
        max_ele = i

print("Minimum element:", min_ele)
print("Maximum element:", max_ele)
