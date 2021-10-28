# Shivali Dalmia
#   inventory.py -> h7-3
#   Solution code (mostly) for a simple inventory tracking program
#     using dictionaries.

def get_command():
    command = input("Enter command: ")
    return command


def add_to_inventory(dict):
    invname = input("Enter name of item to add to inventory: ")
    qty = int(input("Enter quantity of item to add: "))

    if invname in dict:
        dict[invname] += qty
    else:
        dict[invname] = qty

def view_inventory(dict):
    print("%9s -- %s" % ("Item", "Qty"))
    for (k, v) in dict.items():
        print("%9s -- %d" % (k, v))


def remove_inventory(dict):

    invname = input("Enter name of item to delete from inventory: ")
    qty = int(input("Enter quantity of item to remove: "))

    if invname in dict:
        if qty <= dict[invname]:
            if qty == dict[invname]:
                del dict[invname]
            else:
                dict[invname] -= qty
        else:
            print(f"Quantity of '{invname}' item should be less than or equal to {dict[invname]}.Please enter a valid qty.")
    else:
        print(f"'{invname}' item not present in inventory. Please enter a valid item name.")


def main():
    print("Welcome to StuffMaster, v.0.47")

    inventory = {}  # empty dictionary

    while True:  # get command, process command; quit when selected below

        print("Commands are: ")
        print("'A' => Add to inventory")
        print("'V' => View existing inventory")
        print("'R' => Remove from inventory")
        print("'Q' => Quit after showing final inventory")

        # Get the command

        cmd = get_command().upper()[0]

        # Call the appropriate function based on command

        if cmd == 'A':
            add_to_inventory(inventory)
        elif cmd == 'V':
            view_inventory(inventory)
        elif cmd == 'R':
            remove_inventory(inventory)
        elif cmd == 'Q':
            break
        else:
            print("Unknown command: %s => try again." % cmd)

        # If unknown command, complain and prompt for reentry

    # here, we're quitting

    print("Quitting. Final version of inventory is:")

    # print out final version of inventory

    view_inventory(inventory)

    print("Exiting...")


main()


'''
Welcome to StuffMaster, v.0.47
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: A
Enter name of item to add to inventory: apples
Enter quantity of item to add: 47
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: V
     Item -- Qty
   apples -- 47
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: A
Enter name of item to add to inventory: apples
Enter quantity of item to add: 23
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: V
     Item -- Qty
   apples -- 70
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: R
Enter name of item to delete from inventory: apples
Enter quantity of item to remove: 100
Quantity of 'apples' item should be less than or equal to 70.Please enter a valid qty.
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: R
Enter name of item to delete from inventory: apples
Enter quantity of item to remove: 70
Commands are: 
'A' => Add to inventory
'V' => View existing inventory
'R' => Remove from inventory
'Q' => Quit after showing final inventory
Enter command: Q
Quitting. Final version of inventory is:
     Item -- Qty
Exiting...
'''