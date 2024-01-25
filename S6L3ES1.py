import pandas as pd

vini_dataset = pd.read_csv(".\wine.csv")
print(vini_dataset)

#informazioni riassuntive del dataset
print(vini_dataset.describe())

#media
media = vini_dataset.mean(numeric_only = True)
print(media)

#moda
moda = vini_dataset.mode(numeric_only=True)
