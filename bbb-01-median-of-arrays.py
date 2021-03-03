# Find the median of two sorted arrays.
# eg:
# arr1 = [1, 3, 5]
# arr2 = [2, 4, 6]
#
# median(arr1, arr2) = 3.5
import math
def median(arr1, arr2):
    arr1_index = 0
    arr2_index = 0
    combined_arr = []
    while(arr1_index < len(arr1) or arr2_index < len(arr2)):
        if arr1_index >= len(arr1):
            combined_arr.append(arr2[arr2_index])
            arr2_index+=1
            continue
        if arr2_index >= len(arr2):
            combined_arr.append(arr1[arr1_index])
            arr1_index+=1
            continue
        if arr1[arr1_index] < arr2[arr2_index]:
            combined_arr.append(arr1[arr1_index])
            arr1_index+=1
        else:
            combined_arr.append(arr2[arr2_index])
            arr2_index+=1

    total_len = len(arr1) + len(arr2)


    if total_len % 2 == 0:
        return (combined_arr[int(total_len/2)-1]+combined_arr[int(total_len/2)+1]-1)/float(2)
    else:
        return (combined_arr[math.ceil((total_len/float(2)))-1])



# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET
# TODO: NOT FINISHED YET


def median_lgn(arr1, arr2):
    if len(arr1) ==2 and len(arr2) == 2:
        baseCaseArr = arr1 + arr2
        baseCaseArr = sorted(baseCaseArr)
        index = (len(baseCaseArr) /float(2)) -1

        if len(baseCaseArr) % 2 == 0:
            index = int(index)
            return (baseCaseArr[index] + baseCaseArr[index + 1]) / float(2)
        else:
            return baseCaseArr[int(index)]

    arr1Index = len(arr1) /float(2)
    arr2Index = len(arr2) / float(2)
    if arr1[int(arr1Index)] < arr2[int(arr2Index)]:
        # send down right of arr1 and left of arr2
        arr1Index = math.floor(arr1Index)
        arr2Index = math.ceil(arr2Index)
        return median_lgn(arr1[arr1Index:], arr2[:arr2Index])
    else:
        arr1Index = math.ceil(arr1Index)
        arr2Index = math.floor(arr2Index)
        return median_lgn(arr1[:arr1Index], arr2[arr2Index:])

assert median_lgn([1,3,5], [2,4,6]) == 3.5
assert median_lgn([1,3,5, 6], [2,4,6, 7]) == 4.5


#1,2,3,4,5,6,6,7
