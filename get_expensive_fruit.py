def get_expensive_fruit(data:str)->str:
    """
    This function returns the name of the most expensive fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the most expensive fruit
    """
    # your code here
    prices = []
    names = []
    rows = data.split('\n')[1:]
    for row in rows:
        names.append(row.split(',')[0])
        prices.append(float(row.split(',')[1]))
        
    c = prices[0]
    for f in prices:
        if c < f:
            c = f
    
    return names[prices.index(c)]

f = open('fruits.csv', encoding='UTF-8')
d_file = f.read()
print(get_expensive_fruit(d_file))


