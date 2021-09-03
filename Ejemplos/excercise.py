my_list = []
number = 0
while number != 'done':
    number = input("Enter a number: ")
    if not number != 'done':
        continue
    try:
        my_list.append(float(number))
    except ValueError:
        print("Error ¡Type a number!")

print("The list is: ", my_list)
if len(my_list) != 0:
    print("The average of the list is: ", sum(my_list) / (len(my_list)))
