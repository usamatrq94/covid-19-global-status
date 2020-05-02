# Necessary Imports
import os
import pandas as pd
import math
import pandas as pd

files = os.listdir("C://Users/usama/OneDrive/Desktop/github/covid-19-global-status/datasets")  #Checking all the files in the dataset folder
# There should be three files in here, one for confirmed cases, one for deaths and one for recovery.

for x in range(0,len(files)):
    # Declaring necessary Arrays
    NewCases = []  #Declare an array to import New Cases of all countries
    Rate = [] #Declare a array to calculate and store rate of change
    
    # Coding Algo
    # Here we are picking each of the files one by one, selecting last 14 columns and making a new dataframe
    filename = files[x].split('_')[3] #selecting the name of the file
    extension = filename + ".csv"
    Data = os.path.join("C://Users/usama/OneDrive/Desktop/github/covid-19-global-status/datasets", files[x]) #Path to first file
    Dataset= pd.read_csv(Data)
    df2 = Dataset[Dataset.columns[1]]  #Select the countries column
    df1 = Dataset[Dataset.columns[-14:]] #Select the last 14 days history
    com = pd.concat([df2, df1], axis=1) #Merge the dataframe
    countries_u = com['Country/Region'].unique() #Find all the Unique Countries in the dataset
    
    
    # Here we can merging all states data for different states in a country and making one dataframe with all country values
    for y in range(0,countries_u.shape[0]):
        NC = com[com['Country/Region'] == countries_u[y]].sum(axis=0)
        NC.values.reshape(1,15)
        NC[0] = countries_u[y]
        NewCases.append(NC)
    
    Refined = pd.DataFrame(NewCases) #Defing new DataFrame to save results
    
    # Here we are calculating all derivates for 14 columns
    for z in range(0,countries_u.shape[0]):
        data = Refined[Refined['Country/Region'] == countries_u[z]]
        for a in range(1,data.shape[1]-1):
            rate = data.values.tolist()[0][a+1] - data.values.tolist()[0][a]
            Rate.append(rate)
    
    # We are compliling our results here to create relevant data frames
    Rate = pd.DataFrame(Rate)
    show = Rate.values.reshape(len(countries_u),13)
    show = pd.DataFrame(show)
    countries = pd.DataFrame(countries_u)
    Rate = pd.concat([countries,show], axis=1)
    cols = com.columns.values.tolist()
    del cols[1]
    Rate.columns = cols
    AvRate = Rate.mean(axis=1)
    TodayRate = Rate[Rate.columns[-1]]
    Diff = TodayRate - AvRate
    Status = pd.concat([countries, Diff], axis=1)
    output_path = os.path.join("C://Users/usama/OneDrive/Desktop/github/covid-19-global-status/output",extension)
    Status.columns = ['Countries', filename.capitalize()]
    Status.to_csv(output_path, index=False)

# Lasty, we are interested in creating a single dataframe for all results
confirmed = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/confirmed.csv')
deaths = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/deaths.csv')
recovered = pd.read_csv('C://Users/usama/OneDrive/Desktop/covid-19/Output/recovered.csv')
Result = pd.concat([confirmed, deaths['Deaths'], recovered['Recovered']], axis=1)
impact = recovered['Recovered'] - deaths['Deaths']
X = pd.concat([confirmed['Confirmed'], impact], axis=1)
X.columns = ['Confirmed', 'Impact']
X.to_csv("C://Users/usama/OneDrive/Desktop/github/covid-19-global-status/output/all_data.csv")

print("Data preprocessed sucessfully")
