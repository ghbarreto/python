import json

def read_file():
    txt = "static/scripts/MOCK_DATA.json"
    with open(txt) as text:
        file = json.load(text)
    return file

def single_digit(val):
    gender = []
    
    for v in val:
        if v['gender'] not in gender:
            gender.append(v['gender'])
        else:
            continue
    return gender
