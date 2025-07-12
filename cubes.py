import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
plt.style.use('_classic_test_patch')

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values ,s=10)  # Corrected here

# Set chart title and labels.
ax.set_title("Cube of Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cube of values", fontsize=14)

ax.axis([1, 5000, 1, 125000000000])

plt.savefig('cube.png', bbox_inches='tight')
