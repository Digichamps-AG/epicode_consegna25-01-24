import pandas as pd

iris_dataset = pd.read_csv(".\iris.data")

#stampo le prime 5 righe (non ci sono metadati)
print(iris_dataset.head(5))

#stampo i nomi delle colonne (sono dati, non metadati)
print(iris_dataset.columns)

#creo io e importo un csv con i nomi di colonne, perchè nel file indicato su Epicode ci sono mille altre informazioni
#e non è nemmeno formattato come necessario
nomi_iris = pd.read_csv(".\iris_nomi.csv")

#cambio l'intestazione di iris_dataset
iris_dataset = pd.read_csv(".\iris.data", names=nomi_iris.columns)


#stampo il dataset aggiornato
print(iris_dataset)

#stampo un riassunto
print(iris_dataset.describe())

