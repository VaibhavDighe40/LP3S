import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler



# Load the dataset
df = pd.read_csv("sales_data_sample.csv",encoding='latin1')

df.head()

df.shape 

df.describe()

df.info()

df.isnull().sum()

df.dtypes

# Data Preprocessing
df = df.drop(['ADDRESSLINE1', 'ADDRESSLINE2', 'STATUS', 'POSTALCODE', 'CITY', 'TERRITORY', 'PHONE', 'STATE', 'CONTACTFIRSTNAME', 'CONTACTLASTNAME', 'CUSTOMERNAME', 'ORDERNUMBER'], axis=1)
df = pd.concat([df, pd.get_dummies(df['PRODUCTLINE']), pd.get_dummies(df['DEALSIZE'])], axis=1)
df = df.drop(['COUNTRY', 'PRODUCTLINE', 'DEALSIZE'], axis=1)
df['PRODUCTCODE'] = pd.Categorical(df['PRODUCTCODE']).codes
df.drop('ORDERDATE', axis=1, inplace=True)

df.isnull().sum()

df.dtypes

# Elbow Method for Optimal K
distortions = []
for k in range(1, 10):
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(df)
    distortions.append(kmeanModel.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(16, 8))
plt.plot(range(1, 10), distortions, 'bx-')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Distortion')
plt.title('Elbow Method for Optimal K')
plt.show()

# K-Means Clustering
model = KMeans(n_clusters=3, random_state=2)
model.fit(df)
predictions = model.predict(df)

# PCA Visualization
pca = PCA(n_components=2)
reduced_X = pd.DataFrame(pca.fit_transform(df), columns=['PCA1', 'PCA2'])

# Scatter Plot with Cluster Centers
plt.figure(figsize=(14, 10))
plt.scatter(reduced_X['PCA1'], reduced_X['PCA2'])
reduced_centers = pca.transform(model.cluster_centers_)
plt.scatter(reduced_centers[:, 0], reduced_centers[:, 1], color='black', marker='x', s=300)
plt.show()

# Cluster Visualization
reduced_X['Clusters'] = predictions
plt.figure(figsize=(14, 10))
for cluster_num in range(3):
    plt.scatter(reduced_X[reduced_X['Clusters'] == cluster_num].loc[:, 'PCA1'],
                reduced_X[reduced_X['Clusters'] == cluster_num].loc[:, 'PCA2'],
                label=f'Cluster {cluster_num}')

plt.scatter(reduced_centers[:, 0], reduced_centers[:, 1], color='black', marker='x', s=300)
plt.legend()
plt.show() 