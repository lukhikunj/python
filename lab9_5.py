
faculty_names = ['Alexander', 'Bob', 'Christopher', 'David', 'Eleanor', 'Felicity']

long_names = list(filter(lambda name: len(name) > 8, faculty_names))
print("Names with more than 8 characters:", long_names)
