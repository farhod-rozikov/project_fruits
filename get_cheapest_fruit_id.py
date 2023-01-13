import csv

def get_cheapest_fruit_id(data:str)->id:
    """
    This function returns the index of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
    """
    # your code here
    c = 0.0
    lst = []
    
    rows = data.split('\n')[1:]
    
    for row in rows:
        lst.append(float(row.split(',')[1]))
    
    for f in lst:
        if c < f:
            c = f
    
    return lst.index(c)

f = open('fruits.csv', encoding='UTF-8')
d_file = f.read()
print(get_cheapest_fruit_id(d_file))
    