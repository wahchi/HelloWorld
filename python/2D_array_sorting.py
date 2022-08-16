"""
Question:
Sort given 2d array in order of ascending.
Flatten the 2D array, and sort it such that first sort order is the first number, second sort order is the second number
"""
import functools

def sort_2d_array(input_arr):
    total = functools.reduce(lambda a,b: a+b, input_arr)
    return sorted(sorted(total, key=lambda x: int(x.split('-')[1])), key=lambda x: int(x.split('-')[0]))


if __name__ == "__main__":
    input_arr = [
        ['55-29', '55-32', '62-3', '84-38'],
        ['36-84', '23-53', '22-58', '48-15'],
        ['72-80', '48-6', '11-86', '73-23'],
        ['93-51', '55-11', '93-49', '72-10'],
        ['93-66', '71-32', '16-75', '55-9']
    ]
    print(sort_2d_array(input_arr))

