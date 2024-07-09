import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 75000, 80000, 90000]
}

df = pd.DataFrame(data)

df.plot(kind='bar', x='Name', y='Salary', title='Salary of Employees')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.show()
