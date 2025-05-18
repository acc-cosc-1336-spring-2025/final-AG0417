def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    return tuple(
        i + 1 for i in range(len(dna_string1) - len(dna_string2) + 1)
        if dna_string1[i:i+len(dna_string2)] == dna_string2
    )

# im not sure how else to return multiple python parameter without a list. this is all I could come up with
