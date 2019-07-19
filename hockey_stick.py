import random

def get_stock(id):
    return(random.randint(1,300))

class hockey_stick:

    def __init__(self,
                id=False,
                hand=False,
                curve=False,
                flex=False,
                retail_price=0,
                make=False,
                model=False,
                grip=False):
        self.hand = hand
        self.curve = curve
        self.flex = flex
        self.retail_price = retail_price
        self.make = make
        self.model = model
        self.grip = grip
        self.stock = get_stock(id)

    def get_details(self, id=False):
        if id == False:
            print('Please specify a stick')                        
        else:                        
            print('''
Manufacturer: {}                        
Model: {}
Curve: {}
Flex: {}
Hand: {}
Price: ${}
Grip: {}
Quantity: {}
                '''.format(self.make, self.model, self.curve, self.flex, self.hand, self.retail_price, self.grip, self.stock))

    def get_discount(self, coupon=False):
        deal = 0
        message = 'Sorry, you\'re not eligable for any discounts.'
        if coupon == 'FlashDeal':
            deal = 50
        elif coupon == 'MegaDeal':
            deal = 100  
        if deal != 0:
            message = 'You get ${} off! Total price for this stick is now: ${}! Buy it now!'.format(deal, (self.retail_price - deal))
        print(message)               



stick1 = hockey_stick(55, 'Right', 'Ovetchkin', 90, 200, 'Bauer', 'X250', 'slick')

# stick1.get_details(33)

# stick1.get_discount(str(input('Enter a coupon if you have one: ')))


