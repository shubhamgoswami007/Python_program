print("hello")
print("hello")
print("hello")
class category:
    code_c = 2890

    def __init__(self, name):
        self.name = name
        self.code = category.code_c + 15
        category.code_c += 5
        self.no_of_products = 0
	
    def getName(self):
        return self.name

    def display(self):
        print("\nCategory --> ", self.name)
        print("Code --> ", self.code)
        print("No. of products --> ", self.no_of_products)


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
        products.cate = category.getName()
        products.dict.update(
            {products.item: [self.name, self.code, products.cate, self.price]})

    def display(self):
        print("\nProduct: ", self.name)
        print("Code: ", self.code)
        print("Category: ", self.category.name)
        print("Price: ", self.price)


catg1 = category("mobile")
catg2 = category("pen")
catg3 = category("laptop")

prod1 = products("lenovo", catg3, 50000)
prod2 = products("dell", catg3, 30560)
prod3 = products("hp", catg3, 70000)
prod4 = products("cell", catg2, 500)
prod5 = products("razen", catg2, 330)
prod6 = products("z_ball_pen", catg2, 100)
prod7 = products("realme", catg1, 20000)
prod8 = products("mi", catg1, 10000)
prod9 = products("vivo", catg3, 45000)
prod10 = products("apple", catg1, 150000)

print("\nCategory Details:-\n")
catg1.display()
catg2.display()
catg3.display()
print("--------------------------------")

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

print("\nSearch Product with code:-\n---------------------------------")
def check_code():

    while True:
        print("\n1)for display list formate.--\n2)for display Dictionary formate.--\n0)To exit from this loop.-- ")
        a= int(input())
        if a== 1:
            print("\nEnter Product code:-\n---------------------------------\n")
            code = float(input("enter code to search product:- "))
            temp = 0
            for i in products.list_p:
                if i.code == code:
                    temp=1
                    i.display()
                    break
            if temp == 0:
                print("wrong number!")
        if a == 2:
            print("\nEnter Product with code:-\n---------------------------------\n")
            code = float(input("enter product code:- "))
            temp = 0
            print("{:<15} {:<15} {:<15} {:<15}".format("name", "Code", "category",
                                                       "Price\n-------------------------------------------------------"))
            for key, value in products.dict.items():
                name, Code, category, Price = value
                if value[1] == code:
                    print("{:<15} {:<15} {:<15} {:<15}".format(name, Code, category, Price))
                    temp = 1
            if temp == 0:
                print("product not found")
        if a==0:
            break

check_code()
