# Given a list of strings, write a function to get the kth most frequently occurring string.
# questions: will there be multiple substrings with k occurances?
# if yes do I have to return all. I am assuming only one so there are optimizations I have do
from collections import defaultdict
def kthMostFrequent(input_list, kth_count):
    # initialize hash map
    frequency_count = defaultdict(int)

    # interate over list and make entry in hashmap
    for substring in input_list:
        frequency_count[substring] += 1

    # find a key with occurances that match K.

    frequency_count_list = sorted(frequency_count.items(),
                                  key=lambda kv: (kv[1]),
                                  reverse=True)
    try:
        return frequency_count_list[kth_count][0]
    except IndexError:
        return None





assert kthMostFrequent(["a","b","c","a","b","a"], 0) == "a"
assert kthMostFrequent(["a","b","c","a","b","a"], 1) == "b"
assert kthMostFrequent(["a","b","c","a","b","a"], 2) == "c"
assert kthMostFrequent(["a","b","c","a","b","a"], 3) == None