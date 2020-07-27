# ~~~~~~~~~~~~~~~~~ Sum the all items in the list ~~~~~~~~~~~~~~~~~~~
l1 = [1, 2, 3, 4]

# Method 1
sum_l1 = 0
for i in l1:
    sum_l1 = sum_l1 + i
print(sum_l1)

# Method 2
print(sum(l1))

# ~~~~~~~~~~~~ Find the largest number from the list ~~~~~~~~~~~~~~~~
l2 = [2, 43, 10, 2, 5]
# Method 1
largest = max(l2)


def get_max_num_list(*arg):
    max_num = 0
    for i in arg:
        max_num = arg[0]
        if i > max_num:
            max_num = i
    return max_num


largest1 = get_max_num_list(1, 2, 13, 15)
print(largest1)


# ~~~~~~~~~~~~~~~~~~~~~~Find the count of strings whose len is >=2 and first and last character are same ~~~~~~~~~~~~~~
l1 = ['abc', 'xyz', 'aba', '1221']
string_count = 0
for i in l1:
    if len(i) >= 2 and i[0] == i[-1]:
        string_count += 1
print(string_count)
