# im basically using the same code as before
class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    list = []
    file = open("src/question_d/stock_file.dat", "r")
    for line in file:
        items = line.strip().split(" ", 1)
        symbol = items[0]
        company_name = items[1]
        list.append(Stock(symbol, company_name))
    return list
