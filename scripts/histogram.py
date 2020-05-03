import pandas as pd
import matplotlib.pyplot as plt

Geo_results = pd.read_csv('C://Users/usama/OneDrive/Desktop/github/covid-19-global-status/output/status_algo.csv')
Geo_results = Geo_results.sort_values(by=['Prediction'])
Geo_data=pd.concat([Geo_results['Countries'], Geo_results['Status'], Geo_results['Prediction']], axis=1)
Geo_data.columns = ['Country', 'Status', 'Prediction']

Geo_data.loc[Geo_data['Country'] == 'US', 'Country'] = 'United States of America'
#Geo_data[Geo_data['Country'] == 'United States of America']
Geo_results.loc[Geo_results['Countries'] == 'US', 'Countries'] = 'United States of America'
#Geo_results[Geo_results['Countries'] == 'United States of America']

hist,bin_edges = np.histogram(Geo_data['Prediction'])


counts = []
for x in range(0,len(Geo_data['Prediction'].unique())):
    con = Geo_data[Geo_data['Prediction'] == Geo_data['Prediction'].unique()[x]]['Prediction'].count()
    counts.append(con)

plt.figure(figsize=[5,4])

labels = ['Low Risk', 'High Risk', 'Stability', 'Recovery']
plt.bar(labels, counts, width = 0.5, color='#0504aa',alpha=0.7)
plt.grid(axis='y', alpha=0.50)
plt.xlabel('Status',fontsize=2)
plt.ylabel('Frequency',fontsize=2)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Frequency',fontsize=15)
plt.title('Labels Histogram',fontsize=15)
plt.savefig('graphs/histogram.png')
plt.show()