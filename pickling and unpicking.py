import pickle

# Python object
my_dict = {
    "name1": "Nilabh Sahu",
    "name2": "Keshar Jha",
    "name3": "Onkar Setia"
}

# Pickling
dump = pickle.dumps(my_dict)
print(dump)

#unpickling
load = pickle.loads(dump)
print(load)



