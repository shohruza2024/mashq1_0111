#1-misol
my_tuple = (13, 22, 36, 41, 59)
print(f"Tuple: {my_tuple}")

summa = sum(my_tuple)
print(f"Sonlar yig'indisi: {summa}")

#2-misol
my_tuple = (12, 45, 67, 12, 20)
print(f"Tuple: {my_tuple}")

maximum_num = max(my_tuple)
print(f"Eng katta element: {maximum_num}")

#3-misol
first_tup = (20, 21, 56, 89, 16)
print(f"1-tuple: {first_tup}")

second_tup = (67, 89, 23, 45, 67)
print(f"2-tuple: {second_tup}")

list1 = list(first_tup)
list2 = list(second_tup)

list1.extend(list2)

my_tup = tuple(list1)
print(f"Birlashgan tuple'lar: {my_tup}")

#4-misol
my_tuple = (20, 45, 60, 89, 23, 10, 22)
print(f"Tuple: {my_tuple}")

even_num = tuple(filter(lambda x: x % 2 == 0, my_tuple))
print(f"Tuple'dagi juft sonlar: {even_num}")

#5-misol
my_tuple = (20, 45, 60, 89, 23, 10, 22)
print(f"Tuple: {my_tuple}")

kopaytirish = tuple(map(lambda x: x * 2, my_tuple))
print(f"Elementlar: {kopaytirish}")
