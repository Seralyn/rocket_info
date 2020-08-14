from rocket_dictionary import rocketDictionary

dict = {'Ariane 2': {'mass': 23, 'e': 1}, 'OTRAG': {'a': 5, 'b': 2, 'mass': 4}}
#---SOLUTION 1--- 
my_sorted_dict_by_mass = {k: v for k, v in sorted(rocketDictionary.items(), key=lambda x: x[1]['Mass'])}
print(len(rocketDictionary))
print(len(my_sorted_dict_by_mass))
#---SOLUTION 2---
# newd = {}

# for k,v in sorted(dict.items(), key=lambda x: x[1]['mass']):
#     newd[k] = v



# emptyd = {}

# emptyd["somekindofakey"] = "somekindofavalue"