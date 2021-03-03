# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET 

def print_2d(arr_2d):
    for arr in arr_2d:
        print(arr)

def get_subarray(arr_2d, start, len):
    return [arr_1d[start: start+len] for arr_1d in arr_2d[start:start+len]]

def all_true(arr_2d):
    total_true = 0
    height = len(arr_2d)
    width = 0
    for arr_1d in arr_2d:
        width = len(arr_1d)
        total_true += sum(arr_1d)
    if total_true == (width*height):
        return True
    else:
        return False

def subarray(two_d_array):
    pass


# def subarray_with_index(two_d_array, )

print(all_true(
[
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
]

))


# assert subarray([
#     [1, 1, 1, 0],
#     [1, 1, 1, 1],
#     [1, 1, 0, 0]
# ]) == 2
#
# assert subarray([
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]) == 0
#
# assert subarray([
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0]
# ]) == 1
#
#
# assert subarray([
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1]
# ]) == 1

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]


#print_2d(get_subarray(arr, 1, 2))

#sprint_2d([ar[1:1+2] for ar in arr[1:1+2]])