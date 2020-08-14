first_str = "abc"
second_str = "xyz"


def swap_first_letters(str1, str2):
    last_letter_of_first_string = str1[2]
    last_letter_of_second_string = str2[2]
    output1 = str2[0:2] + last_letter_of_first_string 
    output2 = str1[0:2] + last_letter_of_second_string
    return output1 + " " + output2

print(swap_first_letters(first_str, second_str))
