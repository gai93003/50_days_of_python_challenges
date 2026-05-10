############### Extra Challenge: Dictionary of names ################

# You are given a list of names, and you are asked to write a code that returns all the names that start with "S". You code should return a dictionary of all the names that start with "S" and how many times they appear in the dictionary. Here is a list below:

names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Petal", "Sera"]

# You code should return: {"Sasha": 1, "Sera":2}

def dictionay_names(names: dict):
    others = {}

    for name in names:
        if name[0] == "S":
            others.update({name: names.count(name)})

    return others


print(dictionay_names(names))