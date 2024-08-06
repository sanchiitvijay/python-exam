import pandas as pd
import matplotlib.pyplot as plt

iris_data = pd.read_csv('iris.csv')

print("First 5 rows of the dataset:")
print(iris_data.head())

print("\nLast 5 rows of the dataset:")
print(iris_data.tail())

print("\nInformation about the dataset:")
print(iris_data.info())

print("\nOverview of values in each column:")
print(iris_data.describe())

iris_data.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm', title='Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()
