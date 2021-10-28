# Shivali Dalmia
# palindrome.py

from datetime import date,datetime,timedelta

def find_dates(start_date,end_date):
    diff = end_date-start_date
    date_list = []
    for i in range(diff.days + 1):
        curr_date = start_date + timedelta(i)
        date_list.append(curr_date)
    return date_list

def is_palindrome(date_str):
    reverse = ''
    date_str = date_str.replace('/','')
    date_list = list(date_str)
    for index in range(len(date_list)-1,-1,-1):
        reverse += date_list[index]

    if reverse==date_str:
        return True
    else:
        return False

def main():
    start_date = datetime.strptime("01/01/1000","%m/%d/%Y")
    end_date = datetime.strptime("12/31/2999","%m/%d/%Y")

    date_list = find_dates(start_date,end_date) # Find dates between January 1, 1000 through December 31, 2999

    for date_obj in date_list:                  # Check if date is palindrome
        date_str = date_obj.strftime("%m/%d/%Y")
        if is_palindrome(date_str):
            print(date_str)

main()