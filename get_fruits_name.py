import csv
def get_frutis_name(data:str)->list:
    """
    This function returns the name of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits names
    """
    fruits = []
    f = open(data, encoding='UTF-8')
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        fruits.append(row[0])
    return fruits

print(get_frutis_name('fruits.csv'))

    