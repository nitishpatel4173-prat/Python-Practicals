# Practical 22: List slicing  ->  list[start : stop : step]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("List          :", numbers)

print("numbers[2:6]  :", numbers[2:6])      # index 2 to 5
print("numbers[:4]   :", numbers[:4])       # first four elements
print("numbers[5:]   :", numbers[5:])       # from index 5 to the end
print("numbers[-3:]  :", numbers[-3:])      # last three elements
print("numbers[::2]  :", numbers[::2])      # every second element
print("numbers[1::2] :", numbers[1::2])     # every second, starting at index 1
print("numbers[1:8:3]:", numbers[1:8:3])    # index 1 to 7, step 3
print("numbers[::-1] :", numbers[::-1])     # reversed list

copy_list = numbers[:]                      # slicing makes a copy
copy_list[0] = 999
print("Copy changed  :", copy_list)
print("Original safe :", numbers)

numbers[0:2] = [1, 2]                       # replace a slice
print("After numbers[0:2] = [1, 2] :", numbers)
