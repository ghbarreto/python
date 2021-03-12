val = []
count = 0
for i in range(0, 1000):
    if i % 3 == 0:
        val.append(i)
    elif i % 5 == 0:
        val.append(i)
    elif i % 5 == 0 and i % 3 == 0:
        val.append(i)
    else:
        continue

print(f"Multiples are: {val}")
        
for k in val:
    count = k + count
    
print(f"The count is: {count}")
    