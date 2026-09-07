import pandas as pd
import numpy as np
data = {
'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009,
1010, 1011, 1012, 1013, 1014, 1015],
'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop',
'Headphones', 'Mouse', 'Monitor', 'Webcam',
'Keyboard','Laptop', 'Headphones', 'Monitor', 'Mouse','Webcam'],
'category': ['Computers', 'Accessories', 'Accessories',
'Computers', 'Computers', 'Accessories', 'Accessories', 'Computers',
'Accessories', 'Accessories','Computers', 'Accessories', 'Computers',
'Accessories', 'Accessories'],
'price': [1200, 25, 45, 300, 1150, 80, np.nan, 320, 60, 42,
1300, 75, 310, 22, np.nan],
'units_sold': [3, 15, 10, 5, 2, 8, 12, np.nan, 7, 9,1, 6, 4, 20, 5],
'region': ['North', 'South', 'North', 'East', 'West',
'North', 'South', 'East', 'West', 'North',
'East', 'South', 'West', 'North', 'East'],
'customer_rating': [5, 4, 4, 3, 5, 4, np.nan, 3, 4, 5, 5, 4, 3, 4, 4],
}
sales = pd.DataFrame(data)

print(f"A1 question 1 \n {sales.head()}  \n Question2 \n {sales.tail(3)} \n quesion 3 \n {sales.shape} \n  question 4 \n {sales.columns}\n quesion 5 \n {sales.dtypes} \n")

def nullremix(arr):

    if arr.isnull().sum().sum() > 0:
        arr = arr.dropna()

    return arr

print(f"A2 \n {sales.describe()} \n empty data {sales.isnull().sum()} {nullremix(sales)}")


