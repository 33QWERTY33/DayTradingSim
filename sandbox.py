import matplotlib.pyplot as plt

# Set the style to a dark background
plt.style.use('dark_background')

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a plot with light-colored lines and markers
plt.bar(x, y)

# Add labels and title
plt.xlabel('X-axis label', color='lightgray')
plt.ylabel('Y-axis label', color='lightgray')
plt.title('Dark-themed Plot Example', color='lightgray')

# Customize grid color
plt.grid(color='gray')

# Show the plot
plt.show()