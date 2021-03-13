import matplotlib.pyplot as plt

res = []
squares = []

def cubic_numbers():
    for i in range(1, 1000): 
        squares.append(i)
        for values in squares:
            ans = values * values * values
            res.append(ans)


def graphic_num():
    cubic_numbers()
    response = []
    for i in res:
        if i not in response:
            response.append(i)
    return response

def draw():
    response = graphic_num()
    print(squares)
    print(response)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()

    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel('Value', fontsize=14)
    ax.set_ylabel('Square of value', fontsize=14)

    ax.tick_params(axis='both', labelsize=14)

    ax.plot(squares, response, linewidth=3)
    
    plt.show()

draw()
# # print(res)
