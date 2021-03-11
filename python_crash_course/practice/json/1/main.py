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
                
