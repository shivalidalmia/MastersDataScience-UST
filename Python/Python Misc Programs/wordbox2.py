# Shivali Dalmia
# wordbox2.py

def print_wordbox(word):
    word_list = list(word)
    for row in range(len(word_list)):
        for col in range(len(word_list)):
            if row==0:
                print(word_list[col],end="")
            elif row==len(word_list)-1:
                print(word_list[row-col],end="")
            elif col==len(word_list)-1:
                print(word_list[col-row],end="")
            elif row+col==row:
                print(word_list[row],end="")
            else:
                print(" ",end="")
        print()

def main():
    word = input("Enter a word: ").upper()
    if len(word)>0:
        print_wordbox(word)

main()