import re
import pandas as pd
from datetime import datetime, date,timedelta

from Exercise_1_2 import products,category


class Customer:
    def __init__(self, name, email, phone, street, city, state, country, type,company):
        self.name = self.name1(name)
        self.email = self.emailvalid(email)
        self.phone = self.phonevalid(phone)
        self.street = street
        self.city = self.name1(city)
        self.state = self.name1(state)
        self.country = self.name1(country)
        self.company = company
        if type == 'contact' or type == 'billing' or type == 'shipping' or type == 'company':
            self.type = type
        else:
            print("type check")

    def emailvalid(self,eml):
        emal = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if re.search(emal, eml):
            return  eml
        else:
            print("not valid email")
    def phonevalid(self,num1):
        num = '(0|91)?[7-9][0-9]{9}$'
        if re.search(num, num1):
            return num1
        else:
            print("not valid phone number")

    def name1(self, name_check):

        re1 = '^[A-Za-z]*$'
        if re.search(re1, name_check):
            return name_check
        else:
            return False
    def display(self):
        print("name: ", self.name)
        print("Email :" , self.email)
        print("Phone: ", self.phone)
        print("address :",self.street,self.city,self.state,self.country)
        print("type:",self.type)



class order:
    number=1600
    pdtolist=''
    def __init__(self, number,date , company, billing, shipping):
        self.number=number
        self.date = self.check(date)
        self.company = company
        if billing.type == 'billing' and shipping.type == 'shipping':
            self.billing = billing
            self.shipping = shipping
        else:
            print("type check")
        self.order_lines=[]
        self.total_amount=0

    def total(self):
        for i in self.order_lines:
            self.total_amount=self.total_amount+i.subtotal
        print(self.total_amount)

    def display(self):
       print("number:", self.number)
       print("DATE:",self.date,"Company:",self.company.name)
       print("billing-------------------->")
       self.billing.display()
       print("shipping-------------------->")
       self.shipping.display()
       print("order_lines:")
       temp = pd.DataFrame(i.__dict__ for i in self.order_lines)
       temp['order'] = temp['order'].apply(lambda x: x.number)
       temp['product'] = temp['product'].apply(lambda x: x.name)
       print(temp)
       print("total amount:",end='')
       self.total()
       print()
       self.pdtolist = list(temp['product'])

    def check(self, date1):
        try:
            date_obj = datetime.strptime(date1, '%d-%m-%Y')
            if date_obj.date() < date.today():
                print("The date cannot be in the past!")
            else:
                return date_obj
        except Exception as e:
            print(e)


class Orderline:

    def __init__(self, order, Product,quantity):
        self.order = order
        self.product = Product
        self.price = float(Product.price)
        self.quantity = int(quantity)
        self.subtotal = (self.price*self.quantity)
        self.order.order_lines.append(self)
    def display(self):
        print("Product: ", self.product.name)
        print("Quantity: ", self.quantity)
        print("Price: ", self.price)
        print("Total: ", self.subtotal)

if __name__ == "__main__":
    #customer
    DegitalInfo = Customer('shubham', 'degitalinfo123@gmail.in', '9834786543', 'opp trends', 'Rajkot', 'Gujrat',
                           'India','company','')

    goti = Customer('goti', 'gotim311@gmail.com', '8896787508', 'RK Prime', 'Rajkot', 'Gujrat', 'India', 'billing',
                     DegitalInfo)
    jay = Customer('jay', 'jayg345@gmail.com', '8160709740', 'behind RPJ', 'Mumbai', 'Maharashtra', 'India',
                     'shipping',DegitalInfo)
    Dj = Customer("dj", 'dj@gmail.com', '9826519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India',
                      'contact', '')


    Microsof = Customer('veeru', 'veeruth@gmail.com', '9422587690', 'opp trends', 'Surat', 'Gujrat', 'India'
                        ,'company','')
    rocky = Customer('rocky', 'rock3456@gmail.com', '9790668549', 'opp trends', 'Rajkot', 'Gujrat', 'India',  'billing',
                  Microsof)
    rohit = Customer('rohit', 'rohhit@gmail.com', '9800485642', 'opp trends', 'Dallas', 'Texas', 'USA',
                  'shipping',Microsof)

    spider = Customer('meet', 'meet123@gmail.com', '9903885901', 'Astron', 'Rajkot', 'Gujrat', 'India',
                        'company',
                        "")
    kingpin = Customer('kingpin', 'kingpin@gmail.com', '9967885433', 'Narhe', 'Delhi', 'Delhi', 'India', 'billing',
                  spider)
    peter = Customer('peter', 'parker@gmail.com', '9879659900', 'Reynolds', 'Anaheim', 'newyork',
                     'UnitedStates','shipping',spider)

    mobile = category("Vehicle")
    laptop = category("Gadgets")
    stationary = category("Cloths")

    Mobile1 = products("vivo", mobile, 40000)
    Mobile2 = products("Apple", mobile, 150000)
    Laptop1 = products("Lenovo", laptop, 80000)
    Laptop2 = products("Hp", laptop, 50000)
    stationary1 = products("Book", stationary, 50)
    stationary2 = products("pen & pencile", stationary, 100)

    productlist = [Mobile1, Mobile2, Laptop1, Laptop2, stationary1, stationary2]

    order1 = order(1, '22-01-2022', DegitalInfo, goti, jay)
    order1_line1 = Orderline(order1, Mobile1, 5)
    order1_line2 = Orderline(order1, Mobile1, 5)
    order1_line3 = Orderline(order1, Laptop1, 2)
    order1_line4 = Orderline(order1, stationary2, 6)

    order2 = order( 2,'21-01-2022', Microsof, rocky, rohit)
    order2_line2 = Orderline(order2, Laptop2, 1)
    order2_line3 = Orderline(order2, Laptop1, 2)

    order3 = order( 3,'12-01-2022', spider, kingpin, peter)
    order3_line1 = Orderline(order3, stationary1, 5)
    order3_line2 = Orderline(order3, stationary2, 5)
    order3_line3 = Orderline(order3, Laptop1, 2)

    orderlist = [order1, order2, order3]
    for i in orderlist:
        i.display()
