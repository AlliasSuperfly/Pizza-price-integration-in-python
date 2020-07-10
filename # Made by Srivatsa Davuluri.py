# Made by Srivatsa Davuluri
# pizza price integration

type_of_pizza = input("Enter type of Pizza = ")
a = 'veg' or 'Veg' or 'VEG'
b = 'non veg' or 'Non veg' or 'NON VEG'
c = 'small' or 'SMALL' # veg price = 150 |||| non veg price = 200
d  = 'medium' or 'MEDIUM' # veg price = 300 |||| non veg price =  360
e =  'large' or 'LARGE' # veg price = 500 ||| non veg price = 700
if type_of_pizza == a:
    type_of_veg_pizza = input("Enter type of Veg Pizza = ")
    number_of_veg_pizza = int(input("Enter Number of Veg Pizza = "))
    size_of_pizza  = input("Enter Size of Pizza = ")
    if type_of_veg_pizza == c:
        price_small = int(150)
        bill_amount_veg_1 = price_small * number_of_veg_pizza
        print("Bill Amount = ", str(bill_amount_veg_1))
    elif type_of_veg_pizza == d:
        price_medium = int(300)
        bill_amount_veg_2 = price_medium * number_of_veg_pizza
        print("Bill Amount = ", str(bill_amount_veg_2))
    else:
        price_large = int(600)
        bill_amount_veg_3 = price_large * number_of_veg_pizza
        print("Bill Amount = ", str(bill_amount_veg_3))
else:
    type_of_non_veg_pizza = input("Enter type of Non Veg Pizza = ")
    number_of_non_veg_pizza = int(input("Enter Number of Non Veg Pizza = "))
    size_of_pizza  = input("Enter Size of Pizza = ")
    if type_of_non_veg_pizza == c:
        price_small = int(200)
        bill_amount_non_veg_1 = price_small * number_of_non_veg_pizza
        print("Bill Amount = ", str(bill_amount_non_veg_1))
    elif type_of_non_veg_pizza == d:
        price_medium = int(360)
        bill_amount_non_veg_2 = price_medium * number_of_non_veg_pizza
        print("Bill Amount = ", str(bill_amount_non_veg_2))
    else:
        price_large = int(700)
        bill_amount_non_veg_3 = price_large * number_of_non_veg_pizza
        print("Bill Amount = ", str(bill_amount_non_veg_3))




