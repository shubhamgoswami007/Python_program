print("hello")
print("hello")
import pandas as pd
# from tabulate import tabulate
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


class products:
    code_p = 7805
    list_p = []
    dict = {}
    item = 0
    cate = " "

    def __init__(self, name, category, price):
        self.name = name
        self.code = products.code_p + 15
        products.code_p += 5
        self.price = float(price)
        category.no_of_products += 1
        self.category = category
        products.list_p.append(self)
        products.item += 1
        category.products.append(self)
        products.cate = category.getName()
        products.dict.update(
            {products.item: [self.name, self.code, products.cate, self.price]})

    def display(self):
        print("\nProduct: ", self.name)
        print("Code: ", self.code)
        print("Category: ", self.category.name)
        print("Price: ", self.price)


if __name__ == "__main__":

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

    p1 = [
        products("lenovo", Laptop, 50000),
        products("dell", Laptop, 30560),
        products("hp", PC, 70000),
        products("controller", Xbox, 5000),
        products("razen", pen, 330),
        products("z_ball_pen", pen, 100),
        products("honda", Scooters, 40000),
        products("mi", Mobile, 10000),
        products("vivo", Mobile, 45000),
        products("apple", Mobile, 100000),
        products("R15", Scooters, 70000),
        products("Access", Scooters, 40000),
        products("shift", Cars, 150000),
        products("City_honda", Cars, 80000),
        products("nick", Women, 20000),
        products("reebok", men, 80000),
        products("pc_controller", PlayStation, 7000),
        products("VR", PlayStation, 20000)
    ]

    def line(n):
        if n == 1:
            print("-----------------------------------------")
        else:
            print("-------------------------------------------------------")

    print("\nList of Categories")
    line(1)
    for i in object_of_category:
        i.display()
    print("\n\n")

    print("\nProduct Details:- \n")
    print("{:<15} {:<15} {:<15} {:<15}".format(
        "name", "Code", "category", "Price"))
    line(2)
    for key, value in products.dict.items():
        name, Code, category, Price = value
        print("{:<15} {:<15} {:<15} {:<15}".format(
            name, Code, category, Price))

    print("\nProducts details ORDERBY AND GROUPBY")
    line(1)
    tree = Tree()
    tree.create_node("Product Details", 0)

    for i in object_of_category:
        tree.create_node(i.name, i.name, parent=0)
        if i.parent is not None:
            tree.move_node(i.name, i.parent.name)
        for c in i.products:
            tree.create_node(c.name, c.name, parent=i.name)

    tree.show()

    print("\nsorted Product Details ""'High to low'""\n")
    print("{:<15} {:<15} {:<15} {:<15}".format("name", "Code", "category",
                                               "Price"))
    line(2)

    for key, value in sorted(products.dict.items(), key=lambda item: item[1][3], reverse=True):
        name, Code, category, Price = value
        print("{:<15} {:<15} {:<15} {:<15}".format(
            name, Code, category, Price))

    print("\nsorted Product Details ""'low to high'""\n")
    print("{:<15} {:<15} {:<15} {:<15}".format("name", "Code", "category",
                                               "Price"))
    line(2)

    for key, value in sorted(products.dict.items(), key=lambda item: item[1][3]):
        name, Code, category, Price = value
        print("{:<15} {:<15} {:<15} {:<15}".format(
            name, Code, category, Price))

    print("\nSearch Product Details with it code")
    line(1)

    def check_code():

        while True:
            print("\n1)for display list formate.--\n2)for display Dictionary formate.--\n0)To exit from this loop.-- ")
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
                print("{:<15} {:<15} {:<15} {:<15}".format("name", "Code", "category",
                                                           "Price"))
                line(2)
                for key, value in products.dict.items():
                    name, Code, category, Price = value
                    if value[1] == code:
                        print("{:<15} {:<15} {:<15} {:<15}".format(
                            name, Code, category, Price))
                        temp = 1
                if temp == 0:
                    print("product not found")
            if a == 0:
                break

    check_code()
