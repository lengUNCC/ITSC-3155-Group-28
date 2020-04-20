from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = Invoice().inputProduct('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : ")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    markup = Invoice().inputNumber("Markup percent (%) : ")                 #test line
    tax = Invoice().inputNumber("Tax percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")

    result = Invoice().addProduct(qnt, unit_price, discount, markup, tax)        #modified lines with updated parameters
    products[product] = result
    if repeat == "n":
        break

items_in_cart = Invoice().inputProduct(products)
while True:
    checkout = Invoice().inputAnswer("This is your final cart. Are you sure you want to checkout? (y,n)")
    update = Invoice().inputAnswer("Do you want to update the quantity? (y,n) : ")
    qntUpdate = Invoice().inputNumber("Please enter quantity of product : ")

    if checkout == 'y':
        break
    if update == 'n':
        break
#while True:


total_amount = Invoice().totalPurePrice(products)
update_1 = Invoice().updateCart(products, qntUpdate)
print("Your total pure price is: ", total_amount)
print('Updated quantity: ', update_1)


