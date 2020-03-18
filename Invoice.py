class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount, markup):         #update parameter list
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        self.items['markup'] = markup           #add line
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) / 100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalMarkup(self, products):            #Add this method
        total_markup = 0
        for k, v in products.items():
            total_markup += (int(v['qnt']) * float(v['unit_price'])) * float(v['markup']) / 100
        total_markup = round(total_markup, 2)
        self.total_markup = total_markup
        return total_markup

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products) + self.totalMarkup(products)      #update line
        total_pure_price = round(total_pure_price, 2)
        return total_pure_price

    def inputAnswer(selfself, input_value):
        while True:
            userInput = input(input_value)
            if userInput in['v', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput