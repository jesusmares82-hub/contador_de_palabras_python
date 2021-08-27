sum = 0
i = 0
list = [9, 41, 12, 3, 74, 15]

for element in list:
    i = i + 1
    sum = sum + element
promedio = float(sum) / float(i)

print("After", i, sum, float("{:.3f}".format(promedio)))
