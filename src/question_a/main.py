#add import
import question_a

exit = False
while exit == False:
    table = question_a.create_multiplication_table()
    table = question_a.display_multiplication_table(table)
    print(table)

    print("Do you want to exit y/n?")
    quit = input()
    if quit == "y" or exit == "Y":
        exit = True
