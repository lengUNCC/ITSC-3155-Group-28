from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price : $")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    markup = Invoice().inputNumber("Markup percent (%) : ")                 #test line
    tax = Invoice().inputNumber("Tax percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount, markup, tax)        #modified lines with updated parameters
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products)

print("Your total pure price is: $", total_amount)