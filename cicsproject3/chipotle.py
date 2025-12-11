# Author   : Dominik Gielarowiec    
# Email    : digelarowiec@umass.edu 
# Spire ID : 35150500


order1 = (('Hhhdbw Shustsapgk', 'belchertown', 'SUNDAYFUNDAY', 'barbacoa', '', 'pinto', False, 'tomato salsa', 'chili corn salsa', 'tomatillo green chili salsa', 'guacamole', 'queso blanco', 'sour cream'))
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')

def get_protein(order)->int:
    protein_price=0.0
    if order[3].upper() == "chicken".upper():
        protein_price=2.5
    elif order[3].upper() == "steak".upper():
        protein_price=3.5
    elif order[3].upper() == "barbacoa".upper():
        protein_price=3.5
    elif order[3].upper() == "carnitas".upper():
        protein_price=3.0
    elif order[3].upper() == "veggies".upper():
        protein_price=2.5
    else:
        return protein_price
    return protein_price

def get_rice(order):
    rice_price = 0.0
    if order[4]=="white":
        rice_price=2.5
    elif order[4]=="brown":
        rice_price=3.5
    else:
        return rice_price
    return rice_price

def get_beans(order):
    beans_price = 0.0
    if order[5]=="black":
        beans_price=2.5
    elif order[5]=="pinto":
        beans_price=2.5
    else:
        return beans_price
    return beans_price

def get_burrito(order):
    burrito_price = 0.0
    if order[6]==True:
        burrito_price=2.0
    else:
        return burrito_price
    return burrito_price

def get_toppings(order):
    guacamole = 2.75
    tomatosalsa = 2.5
    chilicornsalsa = 1.75
    tomatillogreenchili = 2.0
    sourcream = 2.5
    fajitaveggies = 2.5
    cheese = 2.0
    quesoblanco = 2.75
    toppings_price=0.0
    for i in order[7:]:
        if i == "guacamole":
            if order[3]=="veggies":
                toppings_price+=0.0
            else:
                toppings_price += guacamole
        elif i == "tomato salsa":
            toppings_price += tomatosalsa
        elif i == "chili corn salsa":
            toppings_price += chilicornsalsa
        elif i == "tomatillo green chili salsa":
            toppings_price += tomatillogreenchili
        elif i == "sour cream":
            toppings_price += sourcream
        elif i == "fajita veggies":
            if order[3]=="veggies":
                toppings_price+=0
            else:
                toppings_price += fajitaveggies
        elif i == "cheese":
            toppings_price += cheese
        elif i == "queso blanco":
            toppings_price += quesoblanco
        else:
            return toppings_price
    return toppings_price

def apply_discount(order, sub_total):
    discounted = sub_total
    if order[2]=="MAGIC":
        discounted = sub_total *.95
    elif order[2]== "SUNDAYFUNDAY":
        discounted = sub_total*.9
    elif order[2]=="FLAT3":
        discounted = sub_total-3
    else:
        return discounted
    return discounted

def approximate_time(order):
    time = 0
    if order[1]=="amherst":
        time = 15
    elif order[1]=="north amherst":
        time = 15
    elif order[1]=="south amherst":
        time = 15
    elif order[1]=="hadley":
        time = 15
    elif order[1]=="northampton":
        time = 30
    elif order[1]=="south hadley":
        time = 30
    elif order[1]=="belchertown":
        time = 30
    elif order[1]=="sunderland":
        time = 30
    elif order[1]=="holyoke":
        time = 45
    elif order[1]=="greenfield":
        time = 45
    elif order[1]=="deerfield":
        time = 45
    elif order[1]=="springfield":
        time = 45
    return time


def generate_invoice(order):
    sub_total = get_protein(order)+get_rice(order)+get_beans(order)+get_toppings(order)+get_burrito(order)
    total = apply_discount(order,sub_total)
    saved = sub_total-total
    print(f"Welcome to Chipotle Mexican Grill Hadley, {order[0]}.\n\
Your invoice is displayed below:\n\
Protein: {order[3]} - ${get_protein(order)}\n\
Rice: {order[4]} rice - ${get_rice(order)}\n\
Beans: {order[5]} beans - ${get_beans(order)}\n\
Burrito: {'Yes' if order[6] else 'No'} - ${int(get_burrito(order))}\n\
Toppings: {', '.join(order[7:])} - ${get_toppings(order)}\n\
Subtotal: ${sub_total}\n\
Discount Code: {order[2]}\n\
Total: ${total}\n\
You Save: ${saved}\n\
Your order will be ready in {approximate_time(order)} minutes.\n\
Enjoy your meal and have a good day!")

    

generate_invoice(order1)