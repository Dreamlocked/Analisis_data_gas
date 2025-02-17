# -*- coding: utf-8 -*-
"""
@author: Dreamlocked
"""

# Regresión polinómica

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Importamos todo el dataset
dataset = pd.read_table('2004-2019.tsv')
# Se elimina fechas de muestreo y tiempo e index
dataset_clean = dataset.drop(dataset.columns[[0, 1, 2]], axis='columns')

# Primer filtro, año 2004 -> luego se generaliza para los demás
dataset_clean = dataset_clean.loc[dataset_clean.loc[:, "ANO"] == 2004 ]

# Traducción de portugues a ingles para evitar confusiones
dataset_clean.columns = ['regions',
                     'state',
                     'product',
                     'num_gas_station/stations_consulted',
                     'unit',
                     'mean_market_price',
                     'sd_market_price',
                     'min_market_price',
                     'max_market_price',
                     'mean_price_margin',
                     'coef_variance_market_price',
                     'mean_dist_price',
                     'sd_distribution_price',
                     'min_distribution_price',
                     'max_distribution_price',
                     'coeff_variance_distribution_price',
                     'month',
                     'year']

# Segundo filtro, producto Etanol -> luego se generaliza para los demás
dataset_clean = dataset_clean.loc[dataset_clean.loc[:, "product"] == "ETANOL HIDRATADO"]

# Eliminando columnas innecesarias por el filtro
dataset_clean = dataset_clean.drop(dataset_clean.columns[[2, 3, 4, 17]], axis='columns')

# Corrigiendo tipo de datos
dataset_clean["mean_dist_price"] = pd.to_numeric(dataset_clean["mean_dist_price"]) 

# Graficando en función de Regiones
# Centro Oeste - Etanol - 2004
sns.set_theme(style="whitegrid")
sns.boxplot(x = "state", y = "mean_market_price", data = dataset_clean, linewidth = 1.5)
sns.boxplot(x = "state", y = "mean_dist_price", data = dataset_clean, palette="Set3", linewidth = 0.5)
plt.xticks(rotation=90)
plt.title("Etanol en Centro Oeste - 2004")
plt.ylabel("Media de venta y distribución ($Real)")
plt.show()