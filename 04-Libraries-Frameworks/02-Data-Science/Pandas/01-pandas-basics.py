# Pandas Basics
import pandas as pd

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Tokyo']
}

df = pd.DataFrame(data)
print(df)
print("\nAge column:", df['Age'])

# TODO: Practice data manipulation with Pandas
