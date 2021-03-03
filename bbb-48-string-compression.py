# Given a string, write a function to compress it by shortening every sequence of the same character to that character followed by the number of repetitions. If the compressed string is longer than the original, you should return the original string.
#
# eg.
#
# compress(“a”) = "a"
# compress(“aaa”) = "a3"
# compress(“aaabbb”) = "a3b3"
# compress(“aaabccc”) = "a3b1c3"

def compress(input):
    output = ""
    previous_char = ""
    previous_char_count = 0

    for current_char in input:
        if current_char == previous_char:
            previous_char_count += 1
        else:
            if previous_char_count > 0:
                output += f"{previous_char}{previous_char_count}"
            previous_char = current_char
            previous_char_count = 1


    output += f"{previous_char}{previous_char_count}"

    if len(output) < len(input):
        return output
    else:
        return input


assert compress("a") == "a"
assert compress("aaa") == "a3"
assert compress("aaabbb") == "a3b3"
assert compress("aaabccc") == "a3b1c3"