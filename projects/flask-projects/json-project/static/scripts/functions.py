def single_digit(val):
    gender = []
    
    for v in val:
        if v['gender'] not in gender:
            gender.append(v['gender'])
        else:
            continue
    return gender
