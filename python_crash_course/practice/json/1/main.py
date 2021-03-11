import json

val = "MOCK_DATA.json"

class Read:
    def __init__(self, first_name, last_name, country, city, email, gender, ip_address):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.city = city
        self.email = email
        self.gender = gender
        self.ip_address = ip_address


def __str__(self):
    # c = Read(f"first_name: {m.first_name}, last_name: {m.last_name}")
    with open(val) as read_file:
        values = json.load(read_file)
        for i in values:
            # print(i['first_name'])
            c = Read(i['first_name'], i['last_name'], i['Country'], i['City'], i['email'], i['gender'], i['ip_address'])
            print(c)

# c = __str__("")           
# print(__str__(c))
__str__("")
