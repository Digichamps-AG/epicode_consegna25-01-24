import pandas as pd

vini_dataset = pd.read_csv(".\wine.csv")
#print(vini_dataset)

print(vini_dataset.describe())