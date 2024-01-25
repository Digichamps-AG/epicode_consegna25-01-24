import pandas as pd

vini_dataset = pd.read_csv(".\wine.csv")
print(vini_dataset)

#informazioni riassuntive del dataset
print(vini_dataset.describe())

#conteggio (non contenuto in describe)
print(vini_dataset.count())

#moda (non contenuta in describe)
moda = vini_dataset.mode(numeric_only=True)
