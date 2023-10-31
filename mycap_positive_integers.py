def print_positive_numbers(input_list):
    positive_numbers =[num for num in input_list if num > 0]
    print(','.join(map(str, positive_numbers)))
  
# test case
list1 = [12,-7,5,64,-14]
print("input:",list1,"outpit:",end="")
print_positive_numbers(list1)

list2=[12,14,-95,3]
print("input:",list2,"output:",end="")
print_positive_numbers(list2)    
    