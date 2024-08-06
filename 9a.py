import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris.csv')

plt.figure(figsize=(10, 6))
df.plot(kind='line', subplots=True, layout=(5, 5), figsize=(15, 10), title="Dataset Visualization")
plt.tight_layout()
plt.show()

df.plot.scatter(x = 'sepal.length', y = 'sepal.width', title = "Scatter plot variable for X and Y axis")
plt.show()

plt.scatter(df.index, df['sepal.length'], c='black')
plt.xlabel('Index')

df.plot(kind='hist')
plt.show()