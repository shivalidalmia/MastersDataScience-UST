import re
def stripComments(code):
   # pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|#[^\r\n]*$)"
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|#[^\r\n]*$)"

    return re.sub(pattern,"",code)

def main():
    fname = input("Enter the file name: ")
    fvar = open(fname, 'r')
    f_new = open('strip_'+fname,'w')
    for aline in fvar:
        print(stripComments(aline)+"\n")
        # str = aline.split('#')

main()