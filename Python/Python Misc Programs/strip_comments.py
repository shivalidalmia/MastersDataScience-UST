# Shivali Dalmia
# strip_comments.py
import re
def stripComments(code):

    pattern = r"(\".*?\"|\'.*?\')|(#.*$)" # Creating regular expression for matching ""/'' strings and comments starting with #
    regex = re.compile(pattern)
    def _replace(match):
        if match.group(2) is not None:    # If a comment starting with # is matched an empty string is replaced
            return ""
        else:
            return match.group(1)         # If a quoted string is found it's returned as it is.
    return regex.sub(_replace,code)


def main():
    fname = input("Enter the file name: ")
    fvar = open(fname, 'r')
    f_new = open('strip_'+fname,'w')
    for aline in fvar:
        f_new.write(stripComments(aline)+"\n")

    fvar.close()
    f_new.close()

main()