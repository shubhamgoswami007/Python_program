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

    def __init__(self, name, category, price,stock_at_locations={}):
        self.name = name
        self.code = products.code_p + 15
        self.price = float(price)
        self.category = category
        self.stock_at_locations = stock_at_locations
        products.code_p += 5
        category.no_of_products += 1
        products.list_p.append(self)
        products.item += 1
        category.products.append(self)
        products.cate = category.getName()

        def Merge(dict1, dict2):
            res = {**dict1, **dict2}
            return res

        products.dict.update({products.item: [self.name, self.code, products.cate,
                                              self.price]})




    def display(self):
        print("\nProduct: ", self.name)
        print("Code: ", self.code)
        print("Category: ", self.category.name)
        print("Price: ", self.price)



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

    def getName(self):
        return self.name

class Movement:

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity
        self.display = ''
        try:
            if self.product.stock_at_locations[self.from_location] >= self.quantity:

                qun = self.product.stock_at_locations[self.from_location] - self.quantity
                self.product.stock_at_locations.update({self.from_location: qun})

                if self.to_location in self.product.stock_at_locations:

                    qun1 = self.product.stock_at_locations[self.to_location] + self.quantity
                    self.product.stock_at_locations.update({self.to_location: qun1})

                else:
                    self.product.stock_at_locations.update({self.to_location: self.quantity})

                self.display = f'product quantity :{self.quantity} from {self.from_location.name} to {self.to_location.name}'

            else:
                self.display = f"quantity no: {self.quantity} of {self.product.name} not available {self.from_location.name}"


        except Exception:
            self.display = "no location for that product\n"


    @staticmethod
    def movements_by_product(product):
        flag = 0
        for item in List_of_movement:
            if item.product.name == product.name:
                flag = 1
                print(item.display)

        if flag == 0:
            print("No movements yet.....")




def line(n):
    if n == 1:
        print("-----------------------------------------")
    else:
        print("-------------------------------------------------------")

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

        rajkot = Location("RAJKOT")
        jamnagar = Location("jamnagar")
        ahmedabad = Location("ahmedabad")
        mumbai = Location("mumbai")

        Location_object = [rajkot, jamnagar, ahmedabad, mumbai]


        p1 = [
            products("lenovo", Laptop, 50000,{rajkot: 30, jamnagar: 40, mumbai: 100}),
            products("dell", Laptop, 30560,{rajkot: 100, jamnagar: 40, mumbai: 10}),
            products("hp", PC, 70000, {rajkot: 30, ahmedabad: 100, mumbai: 10}),
            products("controller", Xbox, 5000, {ahmedabad: 30, jamnagar: 40, mumbai: 20}),
            products("razen", pen, 330, {rajkot: 100, mumbai: 40, ahmedabad: 10}),
            products("z_ball_pen", pen, 100, {rajkot: 30, jamnagar: 40, mumbai: 20}),
            products("honda", Scooters, 40000, {rajkot: 30, jamnagar: 100, mumbai: 20}),
            products("mi", Mobile, 10000, {rajkot: 30, ahmedabad: 40, mumbai: 20}),
            products("vivo", Mobile, 45000, {rajkot: 100, ahmedabad: 40, jamnagar: 10}),
            products("apple", Mobile, 100000, {mumbai: 30, ahmedabad: 40, jamnagar: 20}),
            products("R15", Scooters, 70000, {rajkot: 30, mumbai: 100, ahmedabad: 20}),
            products("shift", Cars, 150000, {mumbai: 30, jamnagar: 50, ahmedabad: 10}),
            products("City_honda", Cars, 80000, {rajkot: 30, jamnagar: 50, mumbai: 20}),
            products("nick", Women, 20000, {ahmedabad: 30, jamnagar: 40, rajkot: 10}),
            products("reebok", men, 80000, {ahmedabad: 50, jamnagar: 40, mumbai: 100}),
            products("ps_controller", PlayStation, 7000,{rajkot: 50, jamnagar: 90, mumbai: 10}),
            products("VR", PlayStation, 20000,{ahmedabad: 100, rajkot: 40, mumbai: 10})
        ]
        List_of_movement = [
            Movement(jamnagar, ahmedabad, p1[0], 50),
            Movement(rajkot, ahmedabad, p1[1], 30),
            Movement(ahmedabad, rajkot, p1[2], 20),
            Movement(ahmedabad, rajkot, p1[3], 40),
            Movement(rajkot, ahmedabad, p1[4], 20),
            Movement(jamnagar, rajkot, p1[5], 20),
            Movement(jamnagar, ahmedabad, p1[6], 30),
            Movement(ahmedabad, rajkot, p1[7], 20),
            Movement(rajkot, jamnagar, p1[8], 20),
            Movement(ahmedabad, rajkot, p1[9], 20),
            Movement(mumbai, rajkot, p1[10], 20),
            Movement(jamnagar, rajkot, p1[11], 20),
            Movement(jamnagar, rajkot, p1[12], 20),
            Movement(ahmedabad, mumbai, p1[13], 20),
            Movement(mumbai, rajkot, p1[14], 20),
            Movement(ahmedabad, rajkot, p1[15], 20),
            Movement(ahmedabad, jamnagar, p1[16], 50)
        ]


        print("List of Categories: ")
        line(1)
        for i in object_of_category:
            i.display()
        print("\n\n")
        #------------------------------------------------------
        print("\nProduct Details:- \n")
        print("{:<15} {:<15} {:<15} {:<15}".format("name", "Code", "category", "Price"))
        line(2)
        for key, value in products.dict.items():
            name, Code, category, Price = value
            print("{:<15} {:<15} {:<15} {:<15} ".format(name, Code, category, Price))
        #---------------------------------------------------
        print("\nList of Location: ")
        line(1)
        print("\n")
        for i in Location_object:
            i.display()
        # ---------------------------------------------------

        print("Display Movements between product object ")
        line(1)
        for i in p1:
            print(i.name)
            Movement.movements_by_product(i)
            print("\n-----")
        #------------------------------------------------------
        print("\nnew stock at location")
        line(1)
        for i in p1:
            i.display()
            print('Location: ', end='')
            for key in i.stock_at_locations:
                print(f'{key.name} - {i.stock_at_locations[key]}', end='  ,')
            print('\n')
        print()

        # print('Location: \n', end='')
        # print("{:<15} {:<15}".format("location", "value"))
        # for key in i.stock_at_locations:
        #     print("{:<15} {:<15}".format(key.name, i.stock_at_locations[key]))
        # print('\n')
        #---------------------------------------------------------------
        print("product list by location")
        line(1)
        for i in Location_object:
            print("--------------")
            print("|"+"    "+i.name+"    "+"|")
            print("--------------")
            print("\nProduct Details:-  \n")
            for p in p1:
                if i in p.stock_at_locations:
                    print(f'{p.name}  -  {p.stock_at_locations[i]}','\n  -------  ')
            print()

