def max_num(a, b, c):
    num = [a, b, c]
    return max(num)

# print(max_num(1,5,3))

def mult_list(list):
    x = 1
    for i in list:
        x = x * i
    return x

# print(mult_list([3, 4, 2]))

def rev_string(str):
    return str[::-1]

# print(rev_string("Hello World!"))

def num_within(num, beg, end):
    if num >= beg and num <= end:
        return True
    else:
        return False

# print(num_within(3, 2, 4))
# print(num_within(10, 2, 5))

def pascal(n):
    for i in range(n):
        row = 11 ** (i)
        print(row)


# pascal(5)