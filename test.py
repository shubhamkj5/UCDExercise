import pandas as pd

data= pd.read_csv("country_vaccinations.csv")

print(data.head(5), data.shape)

print(data["country"])