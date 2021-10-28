# Shivali Dalmia
# gene.py
import re

def is_substring_present(seq,substr):

    codon_pos = {}
    is_present = False
    for str in substr:
        indexes = re.finditer(str,seq)
        index_pos = [index.start() for index in indexes]
        index_dvsble_by_3 = [num for num in index_pos if num%3==0]

        if len(index_dvsble_by_3) != 0:
            is_present = True
            codon_pos[str] = index_dvsble_by_3

    return (is_present,codon_pos)


def is_valid_DNA(seq):
    invalid_bases = {}
    valid = True
    valid_bases = ['A','C','G','T']
    for index in range(len(seq)):
        if seq[index] not in valid_bases:
            valid = False
            if seq[index] not in invalid_bases:
                invalid_bases[seq[index]] = [index]
            else:
                invalid_bases[seq[index]].append(index)

    return (valid,invalid_bases)

def is_gene(dna):

    dna_list = list(dna)
    dna_len = len(dna_list)
    stop_codons = ['TAG','TAA','TGA']
    start_codon = 'ATG'
    if "".join(dna_list[0:3]) == start_codon:  # Starts with codon 'ATG'
        if dna_len%3==0:        # Length of sequence is multiple of 3
            if "".join(dna_list[dna_len-3:]) in stop_codons:  # Ends with any stop codons(TAG,TAA,TGA)
                rem_dna = "".join(dna_list[3:dna_len-3])
                check_stop_codons = is_substring_present(rem_dna,stop_codons)  # Check for STOP codons positions
                if check_stop_codons[0]:
                    return (False,"Stop codons present at invalid positions"+str(check_stop_codons[1]))
                else:
                    return (True,"NA")
            else:
                return (False,"Doesn't end with valid stop codons [TAG,TAA,TGA].")
        else:
            return (False,"Length isn't a multiple of 3.")
    else:
        return (False,"Doesn't start with ATG.")

def main():
    dna = input("Enter a DNA seq: ")
    check_validity = is_valid_DNA(dna)
    if check_validity[0]:
        check_gene = is_gene(dna)
        if check_gene[0]:
            print("Is potential gene")
        else:
            print("Is NOT potential gene")
            print(f"Diagnostic information: {check_gene[1]}")
    else:
        print("Not valid DNA")
        print(f"Diagnostic information - Invalid bases entered at respective positions: {check_validity[1]}")

main()