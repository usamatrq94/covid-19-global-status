from sklearn.cluster import KMeans
from numpy.random import default_rng
import pandas as pd
import numpy as np

X = pd.read_csv('C:\\Users\\usama\\OneDrive\\Desktop\\github\\covid-19-global-status\\output\\all_data.csv')
ykm = []
res = []
center = []

np.random.seed(220)

for x in range(0,50):
    km = KMeans(
    n_clusters=4, init='random',
    n_init=500, max_iter=100, 
    tol=x*2, random_state=x
    )
    y_km = km.fit_predict(X)
    ykm.append(y_km)
    
    cents = km.cluster_centers_
    center.append(cents)
    zero = (y_km == 0).sum()
    one = (y_km == 1).sum()
    two = (y_km == 2).sum()
    three = (y_km == 3).sum()
    results_tuple = (zero, one, two, three) 
    res.append(results_tuple)
    
sdev=[]

for x in range(0,len(res)):
    std = np.std(res[x])
    sdev.append(std)

res = pd.DataFrame(res)
sdev = pd.DataFrame(sdev)
rykm = pd.concat([res,sdev], axis=1)
rykm.columns = ['0','1','2','3', 'Stdev']

select = rykm[(rykm['Stdev'] < np.percentile(rykm['Stdev'],5))].sort_values(by='Stdev', ascending=True)
sel = select[select['Stdev'] == select['Stdev'].max()]

y_km = ykm[sel.index[0]]
y_km = pd.DataFrame(y_km)
results = pd.concat([X, y_km], axis=1)
results.columns = ['Strength', 'Impact', 'Prediction']

import matplotlib.pyplot as plt
plt.scatter(results[results['Prediction'] == 0]['Impact'] ,results[results['Prediction'] == 0]['Strength'], s=20, c='red', label='C1')
plt.scatter(results[results['Prediction'] == 1]['Impact'] ,results[results['Prediction'] == 1]['Strength'], s=20, c='blue', label='C1')
plt.scatter(results[results['Prediction'] == 2]['Impact'] ,results[results['Prediction'] == 2]['Strength'], s=20, c='green', label='C1')
plt.scatter(results[results['Prediction'] == 3]['Impact'] ,results[results['Prediction'] == 3]['Strength'], s=20, c='cyan', label='C1')

plt.title('World Covid Cases')
plt.xlabel('Impact')
plt.ylabel('Strength')
plt.savefig('graphs/kmeans.png')
plt.show()

confirmed = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/confirmed.csv')
deaths = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/deaths.csv')
recovered = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/recovered.csv')
Status = pd.concat([confirmed, deaths['Deaths'], recovered['Recovered'], results], axis=1)
pd.to_csv("C://Users/usama/OneDrive/Desktop/github/covid-19-global-status/output/all_data.csv", index=False)
