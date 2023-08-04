# Problem 1 of 5
def max_num(a, b, c):
    nums = [a, b, c]
    max = 0
    for num in nums:
        if num > max:
            max = num
    return max


# Problem 2 of 5
def mult_list(nums_list):
    result = 1
    for num in nums_list:
        result = result * num
    return result


# Problem 3 of 5
def rev_string(string):
    string = string[::-1]
    return string


# Problem 4 of 5
def num_within(num, beg, end):
    if num >= beg and num <= end:
        return True
    else:
        return False


# Problem 5 of 5


def pascal(n):
    rows = 0
    count = 1
    if rows == n:
        return
    else:
        count = count * 2
        pascal(n - 1)
    return count


print(pascal(8))
