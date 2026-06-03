import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

plt.figure(figsize=(8, 6))
plt.plot(df['Month'], df['Sales'], marker='o')
plt.title('Monthly Sales Chart')
plt.xlabel('Month')
plt.ylabel('Sales (in 10k JPY)')
plt.grid(True)

plt.savefig('sales_chart.png')
print('Chart saved as sales_chart.png!')