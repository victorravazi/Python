
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler



base_credit = pd.read_csv('credit_data.csv')

# Escalonamento dos valores

x_credit = base_credit.iloc[:,1:4].values
y_credit = base_credit.iloc[:,4].values

#print(type(y_credit))

#print(x_credit[:,0].min())
#print(x_credit[:,0].max())
#print(x_credit[:,1].min())
#print(x_credit[:,1].max())


scaler_credit = StandardScaler()
x_credit = scaler_credit.fit_transform(x_credit)
#print(scaler_credit.fit_transform(x_credit))

#print(x_credit[:,0].max())
#print(x_credit[:,1].max())
#print(x_credit[:,2].max())

# nova base de dados Census
base_census = pd.read_csv("census.csv")
print(base_census)

