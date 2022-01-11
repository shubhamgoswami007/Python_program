from Exercise_1_3 import products,category

class Location:
    code_l=1200
    def __init__(self,name):
        self.name=name
        self.code=Location.code_l+1
        Location.code_l+=1
    def display1(self):
        print("location name:", self.name, "code", self.code)


class Movement:

    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=quantity
        self.display=''
        try:
            if self.product.stock_at_locations[self.from_location] >= self.quantity:
                qun = self.product.stock_at_locations[self.from_location] - self.quantity
                self.product.stock_at_locations.update({self.from_location: qun})
                if self.to_location in self.product.stock_at_locations:
                    qun1 = self.product.stock_at_locations[self.to_location] + self.quantity  # 10+20
                    self.product.stock_at_locations.update({self.to_location: qun1})  # {ahmedabad,30}

                else:

                    self.product.stock_at_locations.update({self.to_location: self.quantity})

                self.display = f'product quantity :{self.quantity} from {self.from_location.name} to {self.to_location.name}'

            else:
                print(f"quantity no: {self.quantity} of {self.product.name} not available {self.from_location.name}")
        except Exception:
            print("no location for that product\n")


    @staticmethod
    def movements_by_product(product):
        flag = 0
        for item in listofm:
            if item.product.name == product.name:
                flag = 1
                print(item.display)

        if flag == 0:
            print("No movements yet.....")

if __name__ == "__main__":
    rajkot = Location("RAJKOT")
    jamnagar = Location("jamnagar")
    ahmedabad = Location("ahmedabad")
    mumbai = Location("mumbai")
    listofl = [rajkot, jamnagar, ahmedabad, mumbai]
    for i in listofl:
        i.display1()

    device = category("device")

    listofprodcut=[
        products("mobile", device, 12000, {rajkot: 300}),
        products("laptop", device, 230000, {rajkot: 300}),
        products("tablet", device, 1000, {jamnagar: 400}),
        products("television", device, 35000, {jamnagar: 300}),
        products("smart watch", device, 4000, {rajkot: 200})
    ]



    for i in listofprodcut:
        print(i.name)
        for key in i.stock_at_locations:
            print(f'{key.name} - {i.stock_at_locations[key]}')
        print()

    listofm=[
        Movement(rajkot, ahmedabad, listofprodcut[1], 20),
        Movement(rajkot, jamnagar, listofprodcut[2], 20),
        Movement(jamnagar, ahmedabad, listofprodcut[3], 50),
        Movement(jamnagar, rajkot, listofprodcut[4], 30)
    ]

    print("display movement")
    for i in listofprodcut:
        print(i.name)
        Movement.movements_by_product(i)
        print()
    print("\n")
    print("==========")
    print("new stock at location")
    for i in listofprodcut:
        i.display()
        print('Location: ',end='')
        for key in i.stock_at_locations:
            print(f'{key.name} - {i.stock_at_locations[key]}', end='  ')
        print('\n')
    print()


    print("product list by location")
    for i in listofl:
        print(i.name)
        for p in listofprodcut:
            if i in p.stock_at_locations:
                print(f'{p.name} - {p.stock_at_locations[i]}')
        print()