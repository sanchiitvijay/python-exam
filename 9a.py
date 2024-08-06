import matplotlib.pyplot as plt
import pandas as pd
import np


file_path = 'iris.csv'
data = pd.read_csv(file_path)

# Visualize
data.plot()
plt.title('Dataset Visualization')
plt.show()

#Scatter plot
data.plot.scatter(x='column1', y='column2')
plt.title('Scatter Plot between Column1 and Column2')
plt.show()

# Colourfull scatter plot
colors = plt.cm.rainbow(np.linspace(0, 1, len('sepal.length')))

for i, category in enumerate('sepal.length'):
    subset = data[data['column3'] == category]
    plt.scatter(subset['column1'], subset['column2'], color=colors[i], label=category)

plt.title('Scatter Plot with Different Colors')
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.legend()
plt.show()

# Histogram
data['column1'].plot.hist()
plt.title('Histogram of Column1')
plt.xlabel('Column1')
plt.ylabel('Frequency')
plt.show()
