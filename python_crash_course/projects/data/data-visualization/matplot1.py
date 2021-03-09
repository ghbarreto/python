import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(squares)
ax.plot(squares, linewidth=3)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()

print("====================")

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)

ax.set_title('Square numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

print("====================")

x_values = range(1, 10001)

y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches='tight')