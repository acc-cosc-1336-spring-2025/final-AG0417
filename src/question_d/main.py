import question_d

exit = False
while exit == False:
    print("1-Display stock purchase history\n2-Exit")
    choice = input().strip()
    
    if choice == "1":
        list = question_d.get_stock_list()
        print("\nSymbol | Company Name")
        print("----------------------")

        for stock in list:
            symbol = stock.get_symbol()
            company = stock.get_company_name()
            print(symbol + " | " + company)
    elif choice == "2":
        exit = True
    else:
        print("Invalid menu option")