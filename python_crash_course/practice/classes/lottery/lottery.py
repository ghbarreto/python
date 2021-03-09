from random import choice as c

lottery = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd' ]
myticket = '6'
count = 0

while lottery:
    random = c(lottery)
    count = count + 1
    print(f"The winners of the lottery are: {random}")
    if random == myticket:
        print(f"For you to win, the lottery had to happen {count} times")
        break
