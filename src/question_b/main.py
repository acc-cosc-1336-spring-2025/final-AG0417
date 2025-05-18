#add import
import question_b

exit = False
while exit == False:
    print("Please enter a DNA string greater than 8 and no greater than 16")
    # assuming the DNA string is valid
    dna_string1 = input()
    if len(dna_string1) > 8 and len(dna_string1) >= 16:
        print("Please enter a DNA substring of length 4 to search for")
        dna_string2 = input()
        if len(dna_string2) == 4:
            print(question_b.get_most_likely_ancestor_consensus(dna_string1, dna_string2))
        else:
            print("Invalid DNA substring")
    else:
        print("Invalid DNA string")

    print("Do you want to exit y/n?")
    quit = input()
    if quit == "y" or exit == "Y":
        exit = True

