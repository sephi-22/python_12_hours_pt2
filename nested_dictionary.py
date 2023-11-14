#Develop a function that takes a nested dictionary and updates a given value given its key path as a list
#Hint:Use recursion or iteration to navigate the nested dictionaries
def nested_dict_updater (dict,key_path,value):
    current = dict
    for key in key_path[:-1]:
        current = current.setdefault(key,{})
    current[key_path[-1]]=value
    return dict



student_data = {
    'John': {
        'age': 20,
        'grades': {'math': 90, 'english': 85, 'history': 88}
    },
    'Alice': {
        'age': 22,
        'grades': {'math': 78, 'english': 92, 'history': 89}
    },
    'Bob': {
        'age': 21,
        'grades': {'math': 85, 'english': 88, 'history': 75}
    }
}
key_path = ['John','grades','math']
value = 80
print(nested_dict_updater(student_data,key_path,value))