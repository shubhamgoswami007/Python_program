import pandas as pd
from tabulate import tabulate
from treelib import Node, Tree


class category:
    code_c = 2890
    cate_list = []

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.code = category.code_c + 15
        category.code_c += 5
        self.no_of_products = 0
        self.products = []
        self.display_name = self.name
        category.cate_list.append(self)
        self.display_names()

    def getName(self):
        return self.name

    def display_names(self):
        count = self
        while (count.parent != None):
            self.display_name = f'{count.parent.name} > {self.display_name}'
            count = count.parent

    def display(self):
        print("\nCategory --> ", self.name)
        print("Code --> ", self.code)
        print("No. of products --> ", self.no_of_products)
        print("Category parent value --> ", self.display_name)
        if self.no_of_products != 0:
            print("List of Products name:- ")
            for i in self.products:
                print(i.name)


class products():
    code_p = 7805
    list_p = []
    dict = {}
    item = 0
    cate = " "
    stock_at_locations={}

    def __init__(self, name, category, price,location,stock):
        self.name = name
        self.code = products.code_p + 15
        self.price = float(price)
        self.category = category
        self.location = location
        self.stock = float(stock)
        products.code_p += 5
        category.no_of_products += 1
        products.list_p.append(self)
        products.item += 1
        category.products.append(self)
        products.cate = category.getName()
        products.dict.update({products.item: [self.name, self.code, products.cate,
                                              self.price,location.name,self.stock]})
        products.stock_at_locations.update({location.name : [self.stock]})

    def display(self):
        print("\nProduct: ", self.name)
        print("Code: ", self.code)
        print("Category: ", self.category.name)
        print("Price: ", self.price)
        print("Stock: ",self.stock)

    def getName(self):
        return self.name


class Location:
    code_l = 8888

    def __init__(self, name):
        self.name = name
        self.code = Location.code_l + 15
        Location.code_l += 5

    def display(self):
        print("name of location:- ",self.name)
        print("code for location:- ",self.code)
        print("\t--------------------\n")


class Movement:

    def __init__(self, from_location, to_location, quantiy):
        self.from_location = from_location
        self.to_location = to_location
        self.product = products
        self.quantiy = quantiy

    def movements_by_product(products):
        print()


def line(n):
    if n == 1:
        print("-----------------------------------------")
    else:
        print("-------------------------------------------------------")

if __name__ == "__main__":
    def print_value(cat, Loc,prod):
        print("List of Categories: ")
        line(1)
        for i in cat:
            i.display()
        print("\n\n")

        print("\nProduct Details:- \n")
        print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15}".format("name", "Code", "category", "Price","Location","stock"))
        line(2)
        for i in products.stock_at_locations.keys():
            print(i)
        for i in products.stock_at_locations.values():
            print(i)
        print("\nList of Location: ")
        line(1)
        print("\n")
        for i in Loc:
            i.display()
        print("\n")

        print("\nProducts details ORDERBY AND GROUPBY")
        line(1)
        tree = Tree()
        tree.create_node("Product Catalogue", 0)

        for i in cat:
            tree.create_node(i.name, i.name, parent=0)
            if i.parent is not None:
                tree.move_node(i.name, i.parent.name)
            for c in i.products:
                tree.create_node(c.name, c.name, parent=i.name)

        tree.show()

        print("\nsorted Product Details ""'High to low'""\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15}".format("name", "Code", "category", "Price","Location","stock"))
        line(2)

        for key, value in sorted(products.dict.items(), key=lambda item: item[1][3], reverse=True):
            name, Code, category, Price,location,stock = value
            print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15} ".format(name, Code, category, Price,location,stock))


        print("\nsorted Product Details ""'low to high'""\n")
        print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15}".format("name", "Code", "category", "Price","Location","stock"))
        line(2)

        for key, value in sorted(products.dict.items(), key=lambda item: item[1][3]):
            name, Code, category, Price,location,stock = value
            print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15}".format(name, Code, category, Price,location,stock))

        print("\nSearch Product Details with it code")
        line(1)


    def call_obj():
        vehicle = category("Vehicle")
        gadget = category("Gadgets")
        cloths = category("Cloths")
        game = category("Game")
        pen = category("Pen")

        Women = category("Women", cloths)
        men = category("men", cloths)
        Cars = category("Cars", vehicle)
        Scooters = category("Scooters", vehicle)
        Laptop = category("Laptop", gadget)
        PC = category("PC", gadget)
        Mobile = category("Mobile", gadget)
        Xbox = category("Xbox", game)
        PlayStation = category("PlayStation", game)

        maruti = category("maruti", Cars)
        T_shirt = category("T_shirt", men)

        object_of_category = [vehicle, gadget, cloths, game, pen, Women, men, Cars, Scooters,
                              Laptop, PC, Mobile, Xbox, PlayStation, maruti, T_shirt]

        Location1 = Location("Gadgets_Location")
        Location2 = Location("Vehicle_Location")
        Location3 = Location("Cloths_Location")
        Location4 = Location("Game_Location")
        Location5 = Location("pen_Location")

        Location_object = [Location1,Location2,Location3,Location4,Location5]


        p1 = [
            products("lenovo", Laptop, 50000,Location1,200),
            products("dell", Laptop, 30560,Location1,400),
            products("hp", PC, 70000,Location1,200),
            products("controller", Xbox, 5000,Location4,200),
            products("razen", pen, 330,Location5,200),
            products("z_ball_pen", pen, 100,Location5,200),
            products("honda", Scooters, 40000,Location2,200),
            products("mi", Mobile, 10000,Location1,200),
            products("vivo", Mobile, 45000,Location1,200),
            products("apple", Mobile, 100000,Location1,200),
            products("R15", Scooters, 70000,Location2,200),
            products("shift", Cars, 150000,Location2,200),
            products("City_honda", Cars, 80000,Location2,200),
            products("nick", Women, 20000,Location3,200),
            products("reebok", men, 80000,Location3,200),
            products("ps_controller", PlayStation, 7000,Location4,200),
            products("VR", PlayStation, 20000,Location4,200)
        ]

        print_value(object_of_category,Location_object,p1)


    call_obj()


    def check_code():
        while True:
            print("\n1)for display list formate.--\n2)for display Dictionary formate.--"
                  "\n0)To exit from this loop.-- ")
            a = int(input())
            if a == 1:
                print("\nEnter Product code:-\n")
                line(1)
                code = float(input("enter code to search product:- "))
                temp = 0
                for i in products.list_p:
                    if i.code == code:
                        temp = 1
                        i.display()
                        break
                if temp == 0:
                    print("wrong number!")
            if a == 2:
                print("\nEnter Product with code:-\n")
                line(1)
                code = float(input("enter product code:- "))
                temp = 0
                print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15}".format("name", "Code", "category", "Price","Location","stock"))
                line(2)
                for key, value in products.dict.items():
                    name, Code, category, Price,location,stock = value
                    if value[1] == code:
                        print("{:<15} {:<15} {:<15} {:<15} {:<19} {:<15}".format(name, Code, category, Price,location,stock))
                        temp = 1
                if temp == 0:
                    print("product not found")
            if a == 0:
                break

    check_code()
