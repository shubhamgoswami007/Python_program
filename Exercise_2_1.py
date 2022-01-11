
import re


class Customer:
    num = "^[7-9][0-9]{9}$"
    email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    def __init__(self, cname, email, phone, street, city, state, country, company, type):
        self.cname = cname
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.company = company
        self.company_name = []
        self.type = type

        validation = re.compile(Customer.num)
        if not validation.search(self.phone):
            msg = "invalid number!"
            raise ValueError(msg)

        EMAIL_validate = re.compile(Customer.email)
        if not EMAIL_validate.search(self.email):
            msg = "invalid EMAIL!"
            raise ValueError(msg)

    def display_Customer(self):
        print("customer name\t\t:", self.cname)
        print("customer Email\t\t:", self.email)
        print("customer Phone\t\t:", self.phone)
        print("customer Street\t\t:", self.street)
        print("customer City\t\t:", self.city)
        print("customer State\t\t:", self.state)
        print("customer Country\t:", self.country)
        print("customer Company\t:", self.company)
        print("customer Type\t\t:", self.type)


class Order:
    def __init__(self, number, date, company, shipping, billing, total_amount, order_lines):
        self.number = number
        self.date = date
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.tottal_amount = total_amount
        self.order_lines = order_lines
        company.company_name.append(self)


customer1 = [customer("byju's", "bhavinsatani87@gmail.in", "9726100000", "opp trends", "Rajkot", "Gujrat", "India", "Byju's", "company"),
             customer("meet", "meet311@gmail.com", "8866999508", "RK Prime",
                      "Rajkot", "Gujrat", "India", "The Infinity", "billing"),
             customer("jatin", "jatin@gmail.com", "8160709740", "behind RPJ",
                      "Rajkot", "Gujrat", "India", "Emipro", "shipping"),
             customer("krutarth", "krutarth@gmail.com", "9726139748",
                      "opp trends", "Rajkot", "Gujrat", "India", "Microsof", "billing"),
             customer("rohit", "rohhit@gmail.com", "9864795581", "opp trends", "Rajkot", "Gujrat", "India", "sPoint", "Transport")]


for i in customer1:
    i.display_Customer()
    print("\n")
