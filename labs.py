def is_even(num):
    return num % 2 == 0

numbers = [1,56,234,87,4,76,24,69,90,1235]
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# even_numbers = lambda x: x % 2 == 0
# even_numbers = lambda x: is_even(x)



def is_odd(num):
    return num % 2 != 0

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))


odd_nums_function = lambda x: not is_even(x)
odd_numbers_2 = filter(odd_nums_function, numbers)
print(list(odd_numbers_2))


from functools import reduce
total = reduce(lambda running_total, item: item + running_total, [1, 2, 3, 4, 5])
print(total)  # Output: 15

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()