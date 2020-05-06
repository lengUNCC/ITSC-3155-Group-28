from Invoice import Invoice
from termcolor import colored as c

products = {}
total_amount = 0
repeat = ''
print("Invoice Generator")
print("\n")
while True:
    product = input('What is your products ID number: ')
    name = Invoice().productName("What is your product? ")
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    markup = Invoice().inputNumber("Markup percent (%) : ")                 #test line
    tax = Invoice().inputNumber("Sales Tax percent (%) : ")
    #Display product
    print(), print(), print()
    print(c('       Product ID:', 'red'), product, c("  Name:", 'red'), name, c("  Quantity:", 'red'), qnt, c("  Price:", 'red'), unit_price)
    print("--------------------------------------------------------------------------")
    print("                                              ", c("Discount: ", 'red'), discount, "%")
    print("                                              ", c("Markup:   ", 'red'), markup, "%")
    print("                                              ", c("Sales Tax: ", 'red'), tax, "%")

    repeat = Invoice().inputAnswer(c("Would you like to edit the product: (e) \nAdd a new product: (a) \nOr Generate the Invoice: (g) \n","blue"))
    while repeat == "e":
        field = Invoice().inputNumber("Which field number would you like to change? \n 1.ID 2.Name 3.Quantity 4.Price 5.Discount 6.Markup 7.Tax\n")
        if field == 1:
            product = input('What is your products ID: ')
        elif field == 2:
            name = Invoice().productName("What is your product? ")
        elif field == 3:
            qnt = Invoice().inputNumber("Please enter quantity of product : ")
        elif field == 4:
            unit_price = Invoice().inputNumber("Please enter unit price : ")
        elif field == 5:
            discount = Invoice().inputNumber("Discount percent (%) : ")
        elif field == 6:
            markup = Invoice().inputNumber("Markup percent (%) : ")
        elif field == 7:
            tax = Invoice().inputNumber("Sales Tax percent (%) : ")
        else:
            print("Error needs to be a number 1-7")
        # Display product
        print(), print(), print()
        print(c('       Product ID:', 'red'), product, c("  Name:", 'red'), name, c("  Quantity:", 'red'), qnt, c("  Price:", 'red'), unit_price)
        print("--------------------------------------------------------------------------")
        print("                                              ", c("Discount: ", 'red'), discount, "%")
        print("                                              ", c("Markup:   ", 'red'), markup, "%")
        print("                                              ", c("Sales Tax: ", 'red'), tax, "%")

        repeat = Invoice().inputAnswer(
            c("Would you like to edit the product: (e) \nAdd a new product: (a) \nOr Generate the Invoice: (g)\n",
              "blue"))

    result = Invoice().addProduct(name, qnt, unit_price, discount, markup, tax)        #modified lines with updated parameters
    products[product] = result
    if repeat == "g":
        break

total_amount = Invoice().totalPurePrice(products)
print(products)
print("Your total pure price is: ", total_amount)