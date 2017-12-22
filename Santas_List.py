import _random
""" This program will let us know whether each individual has been naughty or nice"""

first_name =("Myles Chi Clifton Deandre Donovan Oswaldo Willian Gregorio Alexander Logan Sol Forest")


first_name = first_name.split(" ")

for name in first_name:
    if name[0] == "M":
        print("{} was Naughty this Year".format(name))

    elif name[-1] == "n":
        print("{} was Nice this Year".format(name))

    else:
        print("{} was Naughty and Nice this Year".format(name))




