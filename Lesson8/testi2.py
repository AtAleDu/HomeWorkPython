import random

def bubble_sort(my_list):
    N = len(my_list)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

def the_Shell_method(my_list):
    inc = len(my_list) // 2
    while inc:
        for index, element in enumerate(my_list):
            while index >= inc and my_list[index - inc] > element:
                my_list[index] = my_list[index - inc]
                index -= inc
            my_list[index] = element
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return my_list

def fast_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        q = random.choice(my_list)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in my_list:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return fast_sort(s_nums) + e_nums + fast_sort(m_nums)

my_list = [64, 34, 25, 12, 22, 11, 90]

bubble_sorted_list = bubble_sort(my_list.copy())
shell_sorted_list = the_Shell_method(my_list.copy())
fast_sorted_list = fast_sort(my_list.copy())

print("Пузырька" + str(bubble_sorted_list))
print("Шелл" + str(shell_sorted_list))
print("Быстрая" + str(fast_sorted_list))
