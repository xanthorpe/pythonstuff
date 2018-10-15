import csv
def minimum_difference(csvfile,firstvalue,secondvalue):
    f = open(csvfile,"r")
    file_data = f.read()
    file_data = file_data.split("\n")
    differences = []
    names = []
    for i in file_data[1:]:
        row = i.split(",")
        first_value = int(row[firstvalue])
        second_value = int(row[secondvalue])
        d = first_value - second_value
        differences.append(d)
    for i in file_data[1:]:
        x = i.split(",")
        name = x[0]
        names.append(name)
    abs_differences = [abs(x) for x in differences]
    name_dictionary = dict(zip(names, abs_differences))
    print(min(name_dictionary.items(), key=lambda x: x[1]))
minimum_difference("/dcs/pg18/u1897477/Downloads/football.csv",5,6)
