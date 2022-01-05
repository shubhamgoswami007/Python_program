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
        self.display_name = ""
        category.cate_list.append(self)

    def getName(self):
        return self.name

    def display_names(self):

        if self.parent and self.parent.parent != None:
            self.display_name = f'{self.parent.parent.name} > {self.parent.name} > {self.name}'

        elif self.parent != None:
            self.display_name = f'{self.parent.name} > {self.name}'

        else:
            self.display_name = f'{self.name}'

    def display(self):
        print("\nCategory --> ", self.name)
        print("Code --> ", self.code)
        print("No. of products --> ", self.no_of_products)
        self.display_names()
        print("Category parent value --> ", self.display_name)
        if self.no_of_products != 0:
            print("List of Products name:- ")
            for i in self.products:
                print(i.name)


class products(category):
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
        products.dict.update({products.item: [self.name, self.code, products.cate, self.price]})

    def display(self):
        print("\nProduct: ", self.name)
        print("Code: ", self.code)
        print("Category: ", self.category.name)
        print("Price: ", self.price)


footwear = category("Footwear")
women = category("Women", footwear)
men = category("men",footwear)
w_shoes = category("Woman_Shoes", women)
m_shoes = category("Man_Shoes", men)

vehicle = category("Vehicle")
car = category("Cars", vehicle)
scooter = category("Scooters", vehicle)
activa = category("Active",vehicle)
automatic = category("Automatic", car)

gadget = category("Gadgets")
laptop = category("Laptop", gadget)
communication = category("Communication",gadget)
wristwatch = category("Wrist watches", gadget)
mobile = category("Mobiles", communication)

pen = category("Pen")



prod1 = products("lenovo", laptop, 50000)
prod2 = products("dell", laptop, 30560)
prod3 = products("hp", laptop, 70000)
prod4 = products("cell", wristwatch, 500)
prod5 = products("razen", pen, 330)
prod6 = products("z_ball_pen", pen, 100)
prod7 = products("honda", scooter, 40000)
prod8 = products("mi", mobile, 10000)
prod9 = products("vivo", mobile, 45000)
prod10 = products("apple", mobile, 100000)
prod11 = products("honda", activa, 50000)
prod12 = products("R15", scooter, 70000)
prod13 = products("Access", activa, 40000)
prod14 = products("shift", car, 150000)
prod15 = products("honda", car, 80000)
prod16 = products("i20", automatic, 70000)
prod17 = products("nick", w_shoes, 20000)
prod18 = products("reebok", m_shoes, 80000)
prod19 = products("nick", w_shoes, 70000)
prod20 = products("nick", m_shoes, 20000)

print("List of Categories")
print("-----------------------------------------")
for i in category.cate_list:
    i.display()
print("\n\n")

print("\nProduct Details:- \n")
print("{:<10} {:<10} {:<10} {:<10}".format("name", "Code", "category",
                                           "Price\n---------------------------------------"))
for key, value in products.dict.items():
    name, Code, category, Price = value
    print("{:<10} {:<10} {:<10} {:<10}".format(name, Code, category, Price))

print("\nsorted Product Details\n")
print("{:<10} {:<10} {:<10} {:<10}".format("name", "Code", "category",
                                           "Price\n---------------------------------------"))

for key, value in sorted(products.dict.items(), key=lambda item: item[1][3], reverse=True):
    name, Code, category, Price = value
    print("{:<10} {:<10} {:<10} {:<10}".format(name, Code, category, Price))

