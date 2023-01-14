import csv

def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits in the list

    args:
        data: CSV file with the fruits data
    returns:
        list of fruits total price
    """
    total = 0
    f = open(data, encoding='UTF-8')
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        total += float(row[1], 2)
    return total

print(get_total_price('fruits.csv'))

    