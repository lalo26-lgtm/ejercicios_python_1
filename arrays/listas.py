# Lista (list)


my_list = [3,1,5,7,8,1,5,2]
print(my_list)
print(type(my_list))

print(my_list[0])
print(my_list[3])
print(my_list[-1])

print(len(my_list))


my_other_list = ['hi', True, 1, 1.3, [10, 11]]
print(my_other_list[4][0])

for i in range(len(my_other_list)):
    print(i, ' -> ', my_other_list[i])

numbers = [1, 2, 3, 4, 5]
numbers.append(15)
numbers.append(53)
print(numbers)
print(numbers)
numbers.pop()
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.clear()
print(numbers)



