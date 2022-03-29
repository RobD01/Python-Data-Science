# given a string, are all characters unique

def unique(string):

    string_list = list(string)
    string_set = set(string_list)
    if len(string_set) == len(string_list):
        print("All unique characters")
    else:
        print("Not unique characters")

string = "ad123"

unique(string)

    