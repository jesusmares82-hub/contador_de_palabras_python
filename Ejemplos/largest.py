#largest_value = -1
my_list = [9, 41, 12, 3, 74, 15]
small_value = "No existen valores"
try:
    small_value = my_list[0]
except:
    print("Error, la lista esta vacia")


for number in my_list:
    if not number < small_value:
        continue
    small_value = number

print("The small values is: ", small_value)
