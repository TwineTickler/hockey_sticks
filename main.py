class hockey_stick:

    def __init__(self, id=False, make=False, model=False, hand=False,
                curve=False, flex=False, price=0):
        self.id = id
        self.make = make
        self.model = model
        self.hand = hand
        self.curve = curve
        self.flex = flex
        self.price = price

    def __repr__(self):
        representation = {'id':self.id,
                        'make':self.make,
                        'model':self.model,
                        'hand':self.hand,
                        'curve':self.curve,
                        'flex':self.flex,
                        'price':self.price}
        return(str(representation)) # hockey_stick() would not return a dict, so I had to cast to a string
