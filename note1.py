emptyd["a"] = "4"


regular_dict = {
        "c": 3,
        "a": 1,
        "d": 4,
        "b": 2,      
        "g": 7,
        "e": 5,
        "h": 8,
        "f": 6
                }


double_dict = {
    "poo":{
        "c": 3,
        "a": 1,
        "d": 4,
        "b": 2      
    },

    "shit":{
        "g": 7,
        "e": 5,
        "h": 8,
        "f": 6
        
        
    },

}

# for v in dict.values():   #dict.keys()/dict.values()/dict.items()
#     #print(k,v)
#     #print(k)
#     print(v)

sort_by_value = sorted((value) for (key,value) in regular_dict.items())
# sorted_d2 = sorted((key, value) for (key,value) in regular_dict.items())
print(sorted_d)
# print(sorted_d2)

# sorted_d3 = sorted((value) for (key, key, value) in double_dict.items())
# print(sorted_d3)