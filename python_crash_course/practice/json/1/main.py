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

def choose_name(self): 
    __str__(self)

def __str__(self):   
    ''' Displays the name '''     
    with open(val) as read_file:
        values = json.load(read_file)
        for i in values:
            c = Read(i['first_name'], i['last_name'], i['Country'], i['City'], i['email'], i['gender'], i['ip_address'])
            # print(f" First name: {c.first_name}\n",f"Last name: {c.last_name}\n", f"Country: {c.country}\n", f"City: {c.city}\n", f"Email: {c.email}\n", f"Gender: {c.gender}\n", f"Ip Address: {c.ip_address}\n =======================")
            for k in self:
                try:
                    if k == c.first_name: 
                        print(f" First name: {c.first_name}\n",f"Last name: {c.last_name}\n", f"Country: {c.country}\n", f"City: {c.city}\n", f"Email: {c.email}\n", f"Gender: {c.gender}\n", f"Ip Address: {c.ip_address}\n =======================")   
                except: 
                    print("Error")
            yield c        
                
def display_all(self): 
    c = __str__("")

    for i in c:
        print(f" First name: {i.first_name}\n",f"Last name: {i.last_name}\n", f"Country: {i.country}\n", f"City: {i.city}\n", f"Email: {i.email}\n", f"Gender: {i.gender}\n", f"Ip Address: {i.ip_address}\n =======================")

def display_country(self):
    c = __str__(self)
    
    for k in c:
        if self == k.country:
            print(f" First name: {k.first_name}\n",f"Last name: {k.last_name}\n", f"Country: {k.country}\n", f"City: {k.city}\n", f"Email: {k.email}\n", f"Gender: {k.gender}\n", f"Ip Address: {k.ip_address}\n =======================")

