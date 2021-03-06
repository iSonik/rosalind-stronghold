
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.

# Sample Dataset
# AAAACCCGGT

# Sample Output
# ACCGGGTTTT


dataset = "CACACACATCACGATGGCTGAGGCGGCATCATGACCTCGCTAGCATAGCCCCTTCAGCTGTGATTCTTGCCAAGACGGTCCCTGACAGCTGGGAAGCCCATAGTTCGGCTTTAAGGTTACCGCCGAGATGACCAAAGACACCAACAAACAGGTGTACAATTTTTTCAGCGCTATACCGGGTACTATGTCCAGGGTAGAAGACTCCGAACGACAATCACACAACGTACGTGCCCAACCATGCTAAGCCCACGGATGAGCCGCAGTACTCAATGTCGCACAAATTGATATTTCTAATTCAAAAATCAGCACTATGCAGGAGACACGGCACATATCATAGAGTGCATTTCCTTTCCCGTGACTATCCAATGTCATGCCAGTTTACTATCGGAACAGACGAAATACGTTCAGCGACCTTACTCGTGGACACTTGCAGGTCTGGAGGGCTGTCTGGAGTCTCAATACCACAATGCATCGGGCAGTCAAGTAGTTATAGCTGTCGATGTTGGAAGTTTTGTGCCTATAGATCGGGCCTCTAGCCAACCTCGATTTGTGGCGCCAATGGCATAGTAGTAGACAGGGCGGGTTCAGGGTGGGTGCTAGCTGTTGATTTCCATACCTCTCATGCGTCTCTTCCCGAGGGTACTAATCATAGTGAGATTTCTATCCGCAACTTTCTGGTGTCAAAGATTTTCTGCAGAGCGCTCTCATATTTCCCCTGGCTGTTCCATATGTCGGGTGGTGCGGACTCTAAGGCCCGCGGTAGTTTGATTAGACCAAAGTGCGAGAACGCTCACTGGCCTTTTTTACCTCATCAACGTGTGCCTTGTTCTACGTAGAGGAGTCCTCGCCACAGGGATTTCTAGTTCAAGGTGGGAGTCAAGGCAACGTAATGGTCGACTTCCTCTGGTATGGAACTCGTGTCAAAGGCGAAGACGTGCCTGAGTGAAGAGATGCGGTTGATGGAGAGC"
dna = dataset[::-1]
complementedStrand = dna.replace("A", "t").replace("G", "c").replace("C", "G").replace("T", "a").upper()
print(complementedStrand)

# Output: 
# GCTCTCCATCAACCGCATCTCTTCACTCAGGCACGTCTTCGCCTTTGACACGAGTTCCATACCAGAGGAAGTCGACCATTACGTTGCCTTGACTCCCACCTTGAACTAGAAATCCCTGTGGCGAGGACTCCTCTACGTAGAACAAGGCACACGTTGATGAGGTAAAAAAGGCCAGTGAGCGTTCTCGCACTTTGGTCTAATCAAACTACCGCGGGCCTTAGAGTCCGCACCACCCGACATATGGAACAGCCAGGGGAAATATGAGAGCGCTCTGCAGAAAATCTTTGACACCAGAAAGTTGCGGATAGAAATCTCACTATGATTAGTACCCTCGGGAAGAGACGCATGAGAGGTATGGAAATCAACAGCTAGCACCCACCCTGAACCCGCCCTGTCTACTACTATGCCATTGGCGCCACAAATCGAGGTTGGCTAGAGGCCCGATCTATAGGCACAAAACTTCCAACATCGACAGCTATAACTACTTGACTGCCCGATGCATTGTGGTATTGAGACTCCAGACAGCCCTCCAGACCTGCAAGTGTCCACGAGTAAGGTCGCTGAACGTATTTCGTCTGTTCCGATAGTAAACTGGCATGACATTGGATAGTCACGGGAAAGGAAATGCACTCTATGATATGTGCCGTGTCTCCTGCATAGTGCTGATTTTTGAATTAGAAATATCAATTTGTGCGACATTGAGTACTGCGGCTCATCCGTGGGCTTAGCATGGTTGGGCACGTACGTTGTGTGATTGTCGTTCGGAGTCTTCTACCCTGGACATAGTACCCGGTATAGCGCTGAAAAAATTGTACACCTGTTTGTTGGTGTCTTTGGTCATCTCGGCGGTAACCTTAAAGCCGAACTATGGGCTTCCCAGCTGTCAGGGACCGTCTTGGCAAGAATCACAGCTGAAGGGGCTATGCTAGCGAGGTCATGATGCCGCCTCAGCCATCGTGATGTGTGTG

# In this case i am converting A to lower case t so that the lower case t is not converted back into an A again at "replace("T", "a")" step
# This is a little bit of a "wonky" solution, but works in this case, a more elegant solution would be to create a dictionary like 
# complement = { "A" : "T", "T" : "A", "C" : "G", "G" : "C"}
# and run a for loop 
