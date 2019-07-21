class hockey_stick:

    def __init__(self, id=False, make=False, hand=False,
                curve=False, flex=False, price=0):
        self.id = id
        self.make = make
        self.hand = hand
        self.curve = curve
        self.flex = flex
        self.price = price

    def __repr__(self):
        representation = {'id':self.id,
                        'make':self.make,
                        'hand':self.hand,
                        'curve':self.curve,
                        'flex':self.flex,
                        'price':self.price}
        return(str(representation)) # hockey_stick() would not return a dict, so I had to cast to a string

    def __str__(self):
        strng = 'id: {}\nmake: {}\nhand: {}\ncurve: {}\nflex: {}\nprice: {}'.format(self.id, self.make, self.hand, self.curve, self.flex, self.price)
        return(strng)

    # Administrator methods:
    # def add_stick(self):
    #     pass
    # def remove_stick(self):
    #     pass
    def 

    # def get_details(self):
    #     pass

    # def purchase_stick(self):
    #     pass

    # Other things to do, first ask if they are a customer or administrator
    # 
    # Administrator can:
    #   - Add new stick to inventory
    #   - Remove stick from inventory
    #   - View inventory
    #   - Change price
    #   - Quit
    #
    # Customer can:
    #   - View inventory
    #   - Purchase Stick
    #   - Quit