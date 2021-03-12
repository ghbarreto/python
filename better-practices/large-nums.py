num1 = 1000000000
num2 = 100000000000000000

total = num1 + num2

print(total)

#* easier way to read numbers

num1 = 1_000_000_000

#* prints 1000000000
#? if I want to print commas(,) then the print should be as follows
print(f'{total:,}')