import question_c

exit = False
while exit == False:
    print("1-Display stock purchase history\n2-Exit")
    choice = input().strip()

    if choice == "1":
        question_c.stock_purchase_history()
    elif choice == "2":
        exit = True
    else:
        print("Invalid menu option")