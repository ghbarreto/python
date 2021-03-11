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


def printin(self):
    with open(val) as read_file:
        print(json.load(read_file))

printin("")
