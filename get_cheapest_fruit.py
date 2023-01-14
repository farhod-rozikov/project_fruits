def get_cheapest_fruit(data:str)->str:
    """
    This function returns the name of the cheapest fruit in the list

    args:
        data: CSV file with the fruits data
    returns:
        name of the cheapest fruit
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
        if c > f:
            c = f
    
    return names[prices.index(c)]

f = open('fruits.csv', encoding='UTF-8')
d_file = f.read()
print(get_cheapest_fruit(d_file))
