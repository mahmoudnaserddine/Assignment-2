#exercise 1
def function(s,i):
    if(i==0):
        return " "
    else:
        reversed = s[::-1]
        for a in range(i):
            print(reversed,end="")

function("mah", 3)


#exercise 2
def function_2(s):
    a=""
    b=""
    for i in s:
        if i.isupper():
            a += i
        else:
            i.islower()
            b += i
    return print(a+b)


function_2("aaBBa")


#exercise 3

def function_3(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
print(function_3("bdc", "cab"))



#exercise 4


def function_4(l):
    max=0
    min=0
    for i in l:
        if i>max:
            max=i
        else:
            if i<min:
                min = i

    print("“the highest value in the list is",max  ,"at index",l.index(max),"”")
    print("“the lowest value in the list is",min, "at index", l.index(min),"”")

function_4(l = [5,6,3,2,7,2,0,1,6],)




#exercise 5

def function_5():
    a=input("input=")
    print(len(a))

function_5()


#exercise 6


def list_jumps(jumps):
    n = len(jumps)
    visited = set()
    current_index = 0

    while current_index >= 0 and current_index < n:
        if current_index in visited:
            return "cycle"

        visited.add(current_index)
        current_index += jumps[current_index]

    return "out-of-bounds"


# Example usage
jumps = [0, -1, 1, -2]
result = list_jumps(jumps)
print(result)





#exercise 7


def add_item(items, barcode, quantity):
    if barcode in items:
        item_name, item_price = items[barcode]
        total_cost = item_price * quantity
        return item_name, quantity, total_cost


def print_receipt(receipt):
    total_amount = 0
    print("\nReceipt:")
    for item in receipt:
        name, quantity, total_cost = item
        receipt_line = "Name: " + name + "\n" + \
                       " - Quantity: " + str(quantity) + "\n" + \
                       " - Total Cost: " + str(total_cost)
        print(receipt_line)
        total_amount += total_cost

    print("Total:", total_amount)


def pos_system():
    items = {
        123: ("Rice-Cakes", 5),
        321: ("Twix", 3)
    }

    while True:
        response = input("Start a new receipt? (yes to start / no to exit): ").lower()

        if response == "no":
            break
        elif response == "yes":
            current_receipt = []

            while True:
                barcode = input("Enter the item barcode (0 to see receipt or restart): ")
                if not barcode.isdigit():

                    print("Invalid input. Please enter a valid number.")
                    continue
                barcode = int(barcode)
                if barcode == 0:
                    break
                if barcode not in items:
                    print("Invalid barcode. Item not found!")
                    continue
                quantity = input("Enter the quantity purchased: ")
                if not quantity.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue
                quantity = int(quantity)
                item = add_item(items, barcode, quantity)
                if item:
                    current_receipt.append(item)

            print_receipt(current_receipt)



pos_system()





