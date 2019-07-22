import datetime
import pandas as pd
currentDT = datetime.datetime.now()

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
    def add_stick(self):
        #build id based off current datetime
        make = str(self.make)
        hand = str(self.hand)
        curve = str(self.curve)
        flex = str(self.flex)
        price = str(self.price)
        newid = str(currentDT.month) + str(currentDT.day) + '-' + str(currentDT.hour) + str(currentDT.minute)
                    # create new dictionary
                    # dict1 = {'id' : newid , 'make' : self.make , 'hand' : self.hand,
                    #     'curve' : self.curve , 'flex':self.flex, 'price':self.price}
                    # with open('database.txt', mode='a+') as f:
                    #     # save new entry to file
                    #     f.write(str(dict1) + '\n')
        insert_string = newid+','+make+','+hand+','+curve+','+flex+','+price+'\n'
        with open('database.csv', mode='a+') as f:
            f.write(insert_string)

    # def remove_stick(self):
    #     pass
    # def modify_price(self):
    #     pass

    # Customer methods:
    # def purchase_stick(self):
    #     pass

    # Shared methods:
    # def view_inventory(self):
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

# First Menu
def init_menu():
    answer = 0
    menu = '''
            Are you an Administrator or a Customer?
            (1) Customer
            (2) Administrator
            (3) Quit

            '''
    answer = int(input(menu))
    while (answer != 1) and (answer != 2) and (answer != 3):
        answer = int(input('Input not accepted. Please enter 1, 2, or 3: '))
    if answer == 1:
        pass # call the customer function

    elif answer == 2:
        pass # call the administrator function
        administrator()
    elif answer == 3:
        pass # exit the program

def administrator():
    answer = 0
    menu = '''
            --- Admin Console ---
            
            What would you like to do?
            (1) View Current Inventory
            (2) Add a Stick
            (3) Remove a Stick
            (4) Edit the Price of a Stick
            (5) Done

            '''
    answer = int(input(menu))
    while (answer != 1) and (answer != 2) and (answer != 3) and (answer != 4) and (answer != 5):
        answer = int(input('Input not accepted. Please enter 1, 2, 3, 4, or 5: '))
    if answer == 1:
        view_inventory()
    elif answer == 2:
        admin_add_a_stick()
    elif answer == 3:
        print('Remove Stick')
    elif answer == 4:
        print('Edit Price')
    elif answer == 5:
        pass # exit the program

def admin_add_a_stick():
    make = str(input('Adding a stick. Enter the following details:\n\nWhat brand is it? '))
    hand = str(input('Is it right of left handed? '))
    curve = str(input('What type of curve does it have? '))
    flex = int(input('What is the flex? '))
    price = float(input('Enter the sale price: '))
    new_stick = hockey_stick(False, make, hand, curve, flex, price)
    new_stick.add_stick()
    print('\nStick has been added!')
    administrator()

def view_inventory():
    df = pd.read_csv('database.csv')
    # df
    # print(df.dtypes)
    # print(df.head)
    # print(df.dtypes)
    cols = df.columns
    print('\n'+cols[0]+'          '+cols[1]+'       '+cols[2]+'        '+cols[3]+'       '+cols[4]+'        '+cols[5])
    print('-----------------------------------------------------------------------')
    for row in range(len(df.index)):
        for i, col in enumerate(range(len(cols))):
            this_many_spaces = ''
            column_span = 12
            current_item = str(df.iat[row,col])
            if i == 5: # add a dollar sign if we're on the last column
                current_item = '$'+str(df.iat[row,col])
            add_this_many_spaces = column_span - len(str(df.iat[row,col])) # how many spaces we'll need to add to space the columns properly
            for spaces in range(add_this_many_spaces):
                this_many_spaces += ' '
            print(current_item, end=this_many_spaces)
        print('\n')
        
    # print(len(cols))
    # print(df.iat[0,1])
    # print(df[cols[0]][0])
    administrator()
    

init_menu()