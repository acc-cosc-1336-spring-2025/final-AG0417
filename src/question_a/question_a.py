x_max = 10
y_max = 5

def create_multiplication_table():
    table = []
    for y in range(1, y_max + 1):   
        row = []
        for x in range(1, x_max + 1): 
            row.append(x * y)
        table.append(row)
    return table

def display_multiplication_table(list):
    table = ""
    for row in list:
        for num in row:
            table += str(num)
        table += "\n"
    return table