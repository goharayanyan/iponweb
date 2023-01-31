# 1) Write a Python program to create a new dictionary by extracting the mentioned keys
# from the below dictionary.
def dict_extract(sample_dict, keys):
    new_dict = {}
    for key in keys:
        new_dict[key] = sample_dict[key]
    return new_dict


d1 = {
    "name": "Kelly",
    "age":  25,
    "salary": 8000,
    "city": "New York"
}
print(dict_extract(d1, ["name", "salary"]))


# 2) Get the key of a minimum value from the following dictionary.
def min_value(dicts):
    value = sorted(dicts.values())[0]
    for key in dicts.keys():
        if dicts[key] == value:
            return key


d2 = {
    "Physics": 82,
    "math": 65,
    "history": 75
}
print(min_value(d2))


# 3) Write a Python program to copy the contents of a file to another file
def copy_content(read_from, write_into):
    with open(write_into, "w") as f2:
        with open(read_from, "r") as f1:
            f2.write(f1.read())
    return "Done"


print(copy_content("file1", "file2"))


# 4)Write a Python program to count the frequency of words in a file
def frequency(file):
    with open(file, "r") as f:
        text = f.read().split()
        dicts = {}
        for word in text:
            if word in dicts:
                dicts[word] += 1
            else:
                dicts[word] = 1
    return dicts


print(frequency("file1"))


# 5) Write a Python program to read last n lines of a file
def last_lines(file, n):
    with open(file, "r") as f:
        length = len(f.readlines())
        f.seek(0)
        for line in range(length-n, length):
            print(f.readline())


print(last_lines("file1", 3))


