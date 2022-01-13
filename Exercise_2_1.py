import re
from datetime import datetime, date, timedelta
from Exercise_1_2 import products, category


class Customer:
    num = "^[7-9][0-9]{9}$"
    email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, name, email, phone, street, city, state, country, type, company):
        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.city = self.name1(city)
        self.state = self.name1(state)
        self.country = self.name1(country)
        self.company = company

        if type == 'contact' or type == 'billing' or type == 'shipping' or type == 'company':
            self.type = type
        else:
            print("type check")

        Number_validation = re.compile(Customer.num)
        if not Number_validation.search(self.phone):
            msg = "invalid number!"
            raise ValueError(msg)

        EMAIL_validate = re.compile(Customer.email)
        if not EMAIL_validate.search(self.email):
            msg = "invalid EMAIL!"
            raise ValueError(msg)

    def name1(self, name_check):
        re1 = '^[A-Za-z]*$'
        if re.search(re1, name_check):
            return name_check
        else:
            return False

    def display(self):
        a=str(self.street)
        b=str(self.city)
        c=str(self.state)
        d=str(self.country)

        print("{:<15} {:<23} {:<15} {:<40} {:<20}".format("Name","Email","Phone","Address","type"))
        address = a+","+b+","+c+","+d
        print("{:<15} {:<23} {:<15} {:<40} {:<20}".format(self.name,self.email,self.phone,address,self.type))





class order:

    Order_dict={}
    month =''
    today = str(date.today())

    def __init__(self, number, date, company, billing, shipping):
        self.number = number
        self.date = self.check(date)
        self.company = company
        if billing.type == 'billing' and shipping.type == 'shipping':
            self.billing = billing
            self.shipping = shipping
        else:
            print("type check")
        self.order_lines = []
        self.list=[]
        self.total_amount = 0

        # order.Order_dict.update(
        #     {self.number: [self.date, self.company.name, self.billing.name, self.shipping.name, Orderline.product, self.total_amount]})

    def total(self):
        self.total_amount=0
        for i in self.order_lines:
            self.total_amount=self.total_amount+i.subtotal
        return self.total_amount

    def check(self, date1):
        try:
            date_obj = datetime.strptime(date1, '%Y-%m-%d')
            if date_obj.date() < date.today():
                print("The date cannot be in the past!")
            else:
                return date_obj
        except Exception as e:
            print(e)




    def display(self):
        print("number:", self.number)
        print("DATE:", self.date)
        print("Company:", self.company.name)
        print("\n\t\t\t------------------------billing--------------------\n")
        self.billing.display()
        print("\n\t\t\t-------------------------shipping--------------------\n")
        self.shipping.display()
        print("\n\t\t-----------------------OrderDetails--------------------\n")
        print("{:<19} {:<15} {:<15} {:<15} {:<15}".format("product Name", "Category", "Price",
                                                          "Quantity", "Sub Total"))
        for i in self.order_lines:
            i.display()
        print("\nTotal Amount:\t",self.total())





class Orderline:

    item = 0
    product=[]
    def __init__(self, order, Product, quantity):
        self.order = order
        self.product = Product
        self.price = float(Product.price)
        self.quantity = int(quantity)
        self.subtotal = (self.price * self.quantity)
        self.order.order_lines.append(self)


    def display(self):
        # print("{:<15} {:<19} {:<15} {:<15} {:<15}".format("number",
        #     "Product name", "price", "Quantity", "Subtotal"))
        #
        # for key, value in Orderline.order_dict.items():
        #     number=key
        #     name, Code, category, Price = value
        #     print("{:<15} {:<19} {:<15} {:<15} {:<15}".format(number,
        #         name, Code, category, Price))

        print("{:<19} {:<15} {:<15} {:<15} {:<15}".format(self.product.name,self.product.category.name ,self.price, self.quantity, self.subtotal))




if __name__ == "__main__":
    def line():
        print("///////////////////////////////////////////////////////////////////////////////////////\n")

    DegitalInfo = Customer('shubham', 'degitalinfo123@gmail.in', '9834786543', 'opp trends', 'Rajkot', 'Gujrat',
                           'India', 'company', '')

    goti = Customer('goti', 'gotim311@gmail.com', '8896787508', 'RK Prime', 'Rajkot', 'Gujrat', 'India', 'billing',
                    DegitalInfo)
    jay = Customer('jay', 'jayg345@gmail.com', '8160709740', 'behind RPJ', 'Mumbai', 'Maharashtra', 'India',
                   'shipping', DegitalInfo)
    Dj = Customer("dj", 'dj@gmail.com', '9826519362', 'Madhavpan', 'Rajkot', 'Gujarat', 'India',
                  'contact', '')

    Microsof = Customer('veeru', 'veeruth@gmail.com', '9422587690', 'opp trends', 'Surat', 'Gujrat', 'India'
                        , 'company', '')
    rocky = Customer('rocky', 'rock3456@gmail.com', '9790668549', 'opp trends', 'Rajkot', 'Gujrat', 'India', 'billing',
                     Microsof)
    rohit = Customer('rohit', 'rohhit@gmail.com', '9800485642', 'opp trends', 'Dallas', 'Texas', 'USA',
                     'shipping', Microsof)

    spider = Customer('meet', 'meet123@gmail.com', '9903885901', 'Astron', 'Rajkot', 'Gujrat', 'India',
                      'company',
                      "")
    kingpin = Customer('kingpin', 'kingpin@gmail.com', '9967885433', 'Narhe', 'Delhi', 'Delhi', 'India', 'billing',
                       spider)
    peter = Customer('peter', 'parker@gmail.com', '9879659900', 'Reynolds', 'Anaheim', 'newyork',
                     'UnitedStates', 'shipping', spider)

    Customer_list = [DegitalInfo, goti, jay, Dj, Microsof, rocky, rohit, spider, kingpin, peter]

    mobile = category("mobile")
    laptop = category("Gadgets")
    stationary = category("stationary")

    Mobile1 = products("vivo", mobile, 40000)
    Mobile2 = products("Apple", mobile, 150000)
    Laptop1 = products("Lenovo", laptop, 80000)
    Laptop2 = products("Hp", laptop, 50000)
    stationary1 = products("Book", stationary, 50)
    stationary2 = products("maps", stationary, 100)

    productlist = [Mobile1, Mobile2, Laptop1, Laptop2, stationary1, stationary2]

    order1 = order(1, '2022-01-13', DegitalInfo, goti, jay)
    order1_line1 = Orderline(order1, Mobile1, 5)
    order1_line2 = Orderline(order1, Mobile1, 5)
    order1_line3 = Orderline(order1, Laptop1, 2)
    order1_line4 = Orderline(order1, stationary2, 6)
    ls=[order1_line1,order1_line2,order1_line3,order1_line4]
    Orderline.product.append(ls)

    order2 = order(2, '2022-02-16', Microsof, rocky, rohit)
    order2_line2 = Orderline(order2, Laptop2, 1)
    order2_line3 = Orderline(order2, Laptop1, 2)

    order3 = order(3, '2022-01-15', spider, kingpin, peter)
    order3_line1 = Orderline(order3, stationary1, 5)
    order3_line2 = Orderline(order3, stationary2, 5)
    order3_line3 = Orderline(order3, Laptop1, 2)

    orderlist = [order1, order2, order3]

    print("Customer Details:- ")
    line()
    for i in Customer_list:
        i.display()
        print("\n")

    print("order Details:- ")
    line()
    for i in orderlist:
        i.display()
        print("\n")


    line()
    print("\t\t\t\tsorting order Details based on date ")
    # print("{:<15} {:<19} {:<15} {:<15} {:<28} {:<15} {:<15}".format("number",
    #     "date", "company", "billing", "shipping","order_line","total_amount"))
    #
    # for key, value in order.Order_dict.items():
    #     number=key
    #     date, company, billing, shipping,orderline,totalamount = value
    #     print("{:<15} {:<19} {:<15} {:<15} {:<15} {:<15} {:<15}".format(number,
    #         date, company, billing, shipping,orderline,totalamount))
    sort = sorted(orderlist,key=lambda item: item.date)
    for i in sort:
        print("-------------*---------------------*--------------------*--------")
        i.display()
        print()
    print("\n")

    line()
    print("\t\t\t\t\torder Details Based on Current Month")
    print("-------------*---------------------*--------------------*--------")
    import datetime
    for i in orderlist:
        var = i.date.month
        today = date.today().month
        if var == today:
            i.display()

    line()
    print("\t\t\t\t\tDisplay all orders of a specific product")
    print("-------------*---------------------*--------------------*--------------")
    for i in productlist:
        print()
        print("order of ", i.name)
        for j in orderlist:
            for r in j.order_lines:
                if r.product == i:
                    print("-------------------")
                    print("order number", j.number)
                    print("{:<19} {:<15} {:<15} {:<15} {:<15}".format("product Name", "Category", "Price",
                                                                      "Quantity", "Sub Total"))

                    r.display()


    line()
    print("Search Order By it's Number")
    print("-------------*---------------------*--------------------*--------------")
    code = int(input("enter number to search product:- "))
    temp = 0
    for i in orderlist:
        if i.number == code:
            temp = 1
            i.display()
            break
    if temp == 0:
        print("wrong number!")

