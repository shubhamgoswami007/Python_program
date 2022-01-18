from Exercise_1_3 import products,category
import os.path

class Location:
    code_l=1200
    def __init__(self,name):
        self.name=name
        self.code=Location.code_l+1
        Location.code_l+=1
    def display1(self):
        print("location name:", self.name, "code", self.code)


class Movement:
    name=''
    def __init__(self,fm,to_location,product,quantity):
        self.from_location=fm
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
    def movements_by_product(product,name):
        flag = 0
        save_path = 'C:/Users/shubh/Desktop/moument_data/'
        for item in listofm:
            Movement.name = item.from_location.name
            completname = os.path.join(save_path,  Movement.name + ".txt")
            if item.product.name == product.name:
                flag = 1
                print(item.display)
                file = open(completname, "a")
                file.write(name+"\n------------\n")
                file.writelines(item.display)
                file.write("\n\n")


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
        products("mobile", device, 12000, {rajkot: 100}),
        products("laptop", device, 230000, {ahmedabad: 100}),
        products("tablet", device, 1000, {jamnagar: 100}),
        products("television", device, 35000, {mumbai: 100}),
        products("smart watch", device, 4000, {rajkot: 100})
    ]



    for i in listofprodcut:
        print(i.name)
        for key in i.stock_at_locations:
            print(f'{key.name} - {i.stock_at_locations[key]}')
        print()

    listofm=[
        Movement(rajkot, ahmedabad, listofprodcut[0], 50),
        Movement(ahmedabad, jamnagar, listofprodcut[1], 60),
        Movement(jamnagar, ahmedabad, listofprodcut[2], 50),
        Movement(mumbai, rajkot, listofprodcut[3], 40),
        Movement(rajkot, mumbai,listofprodcut[4], 70)
    ]

    print("display movement")
    for i in listofprodcut:
        print(i.name)
        Movement.movements_by_product(i,i.name)
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