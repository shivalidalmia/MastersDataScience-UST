# Shivali Dalmia
# theorems.py

'''
(A and (A or B)) == A 	# 'Covering Theorem 1': cover_1(A,B)
'''
def cover_1(A,B):
    return (A and (A or B)) == A

'''
(A or (A and B)) == A 	# 'Covering Theorem 2': cover_2(A,B)
'''
def cover_2(A,B):
    return (A or (A and B)) == A

'''
((A and B) or (A and not B)) == A  	# ('Combining Theorem 1': combine_1(A,B)
'''
def combine_1(A,B):
    return ((A and B) or (A and not B)) == A

'''
((A or B) and (A or not B)) == A  	# 'Combining Theorem 2': combine_2(A,B)
'''
def combine_2(A,B):
    return ((A or B) and (A or not B)) == A

'''
(not (A or B)) == ((not A) and (not B)) 	# ('De Morgan Theorem 1': de_morgan_1(A,B))
'''
def de_morgan_1(A,B):
    return (not (A or B)) == ((not A) and (not B))

'''
(not (A and B)) == ((not A) or (not B)) 	# ('De Morgan Theorem 2': de_morgan_2(A,B))
'''
def de_morgan_2(A,B):
    return (not (A and B)) == ((not A) or (not B))

def main():

    for A in [True,False]:
        for B in [True,False]:
            print(f"[A={A}  B={B}]")
            print(f"Theorem 1: cover_1(A,B): {cover_1(A,B)}")
            print(f"Theorem 2: cover_2(A,B): {cover_2(A,B)}")
            print(f"Combining Theorem 1: combine_1(A,B): {combine_1(A,B)}")
            print(f"Combining Theorem 2: combine_2(A,B): {combine_2(A,B)}")
            print(f"De Morgan Theorem 1: de_morgan_1(A,B): {de_morgan_1(A,B)}")
            print(f"De Morgan Theorem 2: de_morgan_1(A,B): {de_morgan_2(A,B)}\n")

main()


