
#? Unpacking 
a, b = (1, 2)
print(a)
print(b)
#? if not using the second variable, could write like this
a, _ = (1, 2)
print(a)
print(b)
#? number of values cannot exceed the number of variables
#? same goes for the opposite
#! a,b,c = (1,2) | a,b,c = (1,2,3,4) | <- returns an error
#? a,b,c = (1,2,3,4) for this to work, just write it like this
#* a,b, *c = (1,2,3,4) -> Output: a-1 b-2 c-[3,4,5]

#? a,b,*c,d = (1,2,3,4,5) -> output: a-1, b-2, *c-[3,4], d-5
