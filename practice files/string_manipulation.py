# =============================================================================================

a = "Your mother was a hamster and your father smelled of elderberries!"

def count():
    num_of_chars = 0
    for char in a:
        #num_of_chars = num_of_chars + 1
        num_of_chars += 1  #this is better- learn it
    print(num_of_chars)

count()

# =============================================================================================

# %%
a = "Your mother was a hamster and your father smelled of elderberries!"

def count():
    num_of_chars = 0
    for char in a:
        #num_of_chars = num_of_chars + 1
        num_of_chars += 1  #this is better- learn it
    print(num_of_chars)
# %%

# =============================================================================================


def frequency(a):
    dictionary = {}
    for char in a:
        keys = dictionary.keys()
        if char in keys:    
            dictionary[char] = dictionary[char] + 1      # a += 1    a = a + 1
        else:
            dictionary[char] = 1
    return dictionary
print(frequency("Your mother was a hamster and your father smelled of elderberries!"))

# =============================================================================================

#ask Gabi why I can't tell it to print inside the function. I should be fucking able to.
a = "seralyncampbell"
b = "gabrielezarskute"
c = "lizard"
d = "NASA"
e = "AE"
f = "C"
poop = "We are educated"

def front_and_back_combine(string):
    if len(string) < 2:
        return ""                      #originally had return print("")
    
    return string[0:2] + string[-2:]  #originally had return print string[0:2] + string[-2:]

#front_and_back_combine(a)
print(front_and_back_combine(a))
print(front_and_back_combine(b))
print(front_and_back_combine(c))
print(front_and_back_combine(d))
print(front_and_back_combine(e))
print(front_and_back_combine(f))
print(front_and_back_combine(poop))

# =============================================================================================

a = "Your mother was a hamster and your father smelled of elderberries!"
b = "tell me truly if you love testing your toddlers."

def dolla_sign_alteration(str):
    first_letter = str[0]
    #char_to_mod = first_letter.lower()
    str = str.replace(first_letter, "$")
    str = first_letter + str[1:]
    
    return str

print(dolla_sign_alteration(b))
# print(b).replace("t", "$")

# =============================================================================================



def swap_first_letters(str1, str2):
    first_str = "abc"
    second_str = "xyz"
    last_letter_of_first_string = first_str[2]
    last_letter_of_second_string = second_str[2]
    first_str = second_str[0:2] + last_letter_of_first_string 
    second_str = first_str[0:2] + last_letter_of_second_string
    return first_str + " " + second_str

print(swap_first_letters(first_str, second_str))



