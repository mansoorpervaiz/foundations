# # basic solution
# # created sorted list and return kth values
#
# # one pass solution
# # traverse and maintain kth value
#
#
#
# def maintain_k_list(k_list, value, k):
#
#
#     return k_list
#
# # k = 4
# #5,7,6,9,6,10,8,2,4
# # []
# # [5]
# # [7, 5]
# # [7, 5]
# # [
#
# def kth_highest_value_in_list(input_list, kth_value):
#
#     # created sorted list
#     input_list = sorted(input_list, reverse=True)
#     # return kth value while catering for 0 indexing...
#     try:
#         kth_value = kth_value-1
#         if kth_value < 0:
#             raise IndexError
#         return input_list[kth_value]
#     except IndexError:
#         return None
#
#
#
# assert kth_highest_value_in_list([1,2,3,4,5,6,7,8,9,10], 3) == 8
# assert kth_highest_value_in_list([1,3,5,7,9,6,10,8,2,4], 2) == 9
# assert kth_highest_value_in_list([1,3,5,7,9,6,10,8,2,4], -1) == None
# assert kth_highest_value_in_list([1,3,5,7,9,6,10,8,2,4], 11) == None

key_value = {}

# Initializing the value
key_value[2] = 56
key_value[1] = 2
key_value[5] = 12
key_value[4] = 24
key_value[6] = 18
key_value[3] = 323

print(key_value)
print(sorted(key_value.items(),
             reverse=True,
             key=lambda kv: (kv[1])))
from operator import itemgetter, attrgetter
print(sorted(key_value.items(),
             reverse=True,
             key=itemgetter(1)))

