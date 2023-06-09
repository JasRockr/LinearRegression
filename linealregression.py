# -*- coding: utf-8 -*-
"""LinealRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r2Lka4oxsjfPPMNnW-8mp4KeqOInxkgI
"""

# Regresión Líneal Simple
# Prediccion de precios de venta

# https://github.com/gonzalezgouveia/clases-youtube/tree/main/proyecto-house-price
# https://www.youtube.com/watch?v=b7gOUbSmGIY&t=2s

# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
# Lectura de dataset
train = pd.read_csv('./train.csv')
#test = pd.read_csv('./test.csv')

train.head(3)

train.columns

# Columnas de los datos de estudio
train[['GrLivArea','SalePrice']].head()
# X = Area (input) Y = Precio de venta

# Gráfica con los datos de estudio para visualización
train.plot.scatter(x='GrLivArea',y='SalePrice')
plt.show()

# Pintar una línea recta sobre los datos

# Obtener el mínimo de los datos
train['GrLivArea'].min()

# Parámetros de la recta
# w / m / a
w = 118
b = 0

# Puntos de la recta
x = np.linspace(0,train['GrLivArea'].max(),100)
y = w*x+b

# Gráfica de la recta
train.plot.scatter(x='GrLivArea',y='SalePrice')
plt.plot(x, y, '-r')
plt.ylim(0,train['SalePrice'].max()*1.1)
#plt.grid()
plt.show()

# Calcular el error  con los parametros elegidos para el modelo

# Cálculo de las predicciones

#Pred = Train Dataset * w (125) + b (0)
train['pred'] = train['GrLivArea']*w+b

# Cálculo de la función de error (ECM = Error Cuadrático Medio)
# Avg de errores al cuadrado, es decir, diff entre el estimador y lo que se estima
train['diff'] = train['pred']-train['SalePrice']
train['cuad'] = train['diff']**2
train.head()

# Cálculo del valor ECM
train['cuad'].mean()

# Grid de la funcion de error basado en m, b=0
# Encontrar un W óptimo
w = np.linspace(50,200,50)
grid_error = pd.DataFrame(w, columns=['w'])
grid_error.head()

def sum_error(w, train):
    b=0
    train['pred'] = train['GrLivArea']*w+b
    train['diff'] = train['pred']-train['SalePrice']
    train['cuad'] = train['diff']**2
    return(train['cuad'].mean())

grid_error['error']=grid_error['w'].apply(lambda x: sum_error(x, train=train))
grid_error.head()

# Hallar el minimo
grid_error.plot(x='w',y='error')
plt.show()

# usando sklear para saber los valores optimos
from sklearn.linear_model import LinearRegression

# definiendo input y output
X_train = np.array(train['GrLivArea']).reshape((-1, 1))
Y_train = np.array(train['SalePrice'])

# creando modelo
model = LinearRegression(fit_intercept=False)
model.fit(X_train, Y_train)

# imprimiendo parametros
print(f"intercepto (b): {model.intercept_}")
print(f"pendiente (w): {model.coef_}")