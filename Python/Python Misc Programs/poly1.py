# Shivali Dalmia
# poly1.py
# Assuming the length of both coefficient lists are same(polynomials are of same degree)

# Adding elements at each index
def add_coeff(pCoeffList,qCoeffList):
    res_list = [pCoeffList[i]+qCoeffList[i] for i in range(len(pCoeffList))]
    return res_list

# Multiplying each element of list pCoeffList with all elements of qCoeffList
def mul_coeff(pCoeffList,qCoeffList):
    res_list = []
    for p in range(len(pCoeffList)):
        for q in range(len(qCoeffList)):
            if p+q<len(res_list):
                res_list[p + q] = res_list[p+q] + (pCoeffList[p] * qCoeffList[q])
            else:
                res_list.insert(p+q,pCoeffList[p]*qCoeffList[q])

    return res_list

def main():

    pCoeffList = eval(input("Enter the coefficients for p(x) as L[0], L[1], L[2],...:"))
    qCoeffList = eval(input("Enter the coefficients for q(x) as L[0], L[1], L[2],...:"))
    print(f"p(x)+q(x): {add_coeff(pCoeffList,qCoeffList)}")
    print(f"p(x)*q(x): {mul_coeff(pCoeffList,qCoeffList)}")

main()

'''
1,3,4
1,2,1
'''