import pandas as pd
confirmed = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/confirmed.csv')
deaths = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/deaths.csv')
recovered = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/recovered.csv')
Result = pd.concat([confirmed, deaths['Deaths'], recovered['Recovered']], axis=1)
impact = recovered['Recovered'] - deaths['Deaths']
tup = pd.concat([confirmed['Confirmed'], impact], axis=1)
tup.columns = ['Confirmed', 'Impact']

pred = []
status = []

for x in range(0,tup.shape[0]):
    if tup.iloc[x][0] > 0:
        if tup.iloc[x][1] > 0: 
            pred.append(2)
            status.append("Stabilization")

        else:
            pred.append(3)
            status.append("Recovery")
    else:
        if tup.iloc[x][1] > 0:
            pred.append(0)
            status.append("Low Risk")
        else:
            pred.append(1)
            status.append("High Risk")

pred = pd.DataFrame(pred)
status = pd.DataFrame(status)
Status_algo = pd.concat([Result, tup, pred, status], axis=1)

Status_algo.columns = ['Countries', 'dConfirmed', 'dDeath', 'dRecovered', 'Strength', 'Impact', 'Prediction', 'Status']

plt.scatter(Status_own[Status_own['Prediction'] == 0]['Impact'] ,Status_own[Status_own['Prediction'] == 0]['Strength'], s=20, c='red', label='C1')
plt.scatter(Status_own[Status_own['Prediction'] == 1]['Impact'] ,Status_own[Status_own['Prediction'] == 1]['Strength'], s=20, c='blue', label='C1')
plt.scatter(Status_own[Status_own['Prediction'] == 2]['Impact'] ,Status_own[Status_own['Prediction'] == 2]['Strength'], s=20, c='green', label='C1')
plt.scatter(Status_own[Status_own['Prediction'] == 3]['Impact'] ,Status_own[Status_own['Prediction'] == 3]['Strength'], s=20, c='cyan', label='C1')

plt.axis([-750,750,-2000,2000])

plt.title('World Covid Cases')
plt.xlabel('Impact')
plt.ylabel('Strength')
plt.savefig('graphs/algo.png')
plt.show()